from __future__ import annotations

import argparse
import importlib.resources
import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Sequence

from esolang_bench.benchmarking.config import LANGUAGE_METADATA
from esolang_bench.benchmarking.dataset_loader import Problem
from esolang_bench.benchmarking.output_utils import outputs_match_lang
from esolang_bench.interpreters import get_interpreter


@dataclass(frozen=True)
class TestCaseResult:
    index: int
    stdin: str
    expected_output: str
    actual_output: str
    error_type: str
    stderr: str
    passed: bool


@dataclass(frozen=True)
class SolutionValidation:
    language_id: str
    problem: Problem
    solution_path: Path | None
    cases: list[TestCaseResult]

    @property
    def total_tests(self) -> int:
        return len(self.cases)

    @property
    def passed_tests(self) -> int:
        return sum(1 for case in self.cases if case.passed)

    @property
    def failed_cases(self) -> list[TestCaseResult]:
        return [case for case in self.cases if not case.passed]

    @property
    def passed(self) -> bool:
        return self.passed_tests == self.total_tests


def _default_dataset_path() -> Path:
    return Path(str(importlib.resources.files("esolang_bench.data") / "esolang_benchmark.json"))


def _default_solutions_root() -> Path:
    cwd_root = Path.cwd() / "solutions"
    if cwd_root.exists():
        return cwd_root
    return Path(__file__).resolve().parent.parent / "solutions"


@lru_cache(maxsize=None)
def _load_problem_map_cached(dataset_path_str: str) -> dict[str, Problem]:
    path = Path(dataset_path_str)
    raw = json.loads(path.read_text(encoding="utf-8"))
    problem_map: dict[str, Problem] = {}
    for entry in raw.get("problems", []):
        tests = entry.get("input_output_examples") or entry.get("tests") or []
        normalized_tests = [
            {"input": test.get("input", ""), "output": test.get("output", "")}
            for test in tests
        ]
        problem = Problem(
            id=entry.get("id", ""),
            title=entry.get("title", ""),
            description=entry.get("description", ""),
            difficulty=entry.get("difficulty", "unknown"),
            tests=normalized_tests,
        )
        problem_map[problem.id.upper()] = problem
    return problem_map


def load_problem(problem_id: str, dataset_path: Path | None = None) -> Problem:
    path = dataset_path or _default_dataset_path()
    problem_map = _load_problem_map_cached(str(path.resolve()))
    key = problem_id.upper()
    if key not in problem_map:
        raise ValueError(f"Unknown problem id '{problem_id}' in dataset {path}")
    return problem_map[key]


def resolve_solution_path(
    language_id: str,
    problem_id: str,
    solutions_root: Path | None = None,
) -> Path:
    root = solutions_root or _default_solutions_root()
    problem_dir = root / language_id / problem_id.upper()
    if not problem_dir.is_dir():
        raise FileNotFoundError(f"Solution directory not found: {problem_dir}")

    candidates = sorted(path for path in problem_dir.glob("solution.*") if path.is_file())
    if not candidates:
        raise FileNotFoundError(f"No solution.* file found in {problem_dir}")
    if len(candidates) > 1:
        joined = ", ".join(str(path.name) for path in candidates)
        raise ValueError(f"Multiple solution files found in {problem_dir}: {joined}")
    return candidates[0]


def validate_solution_code(
    language_id: str,
    problem: Problem,
    code: str,
    *,
    solution_path: Path | None = None,
    timeout_seconds: float = 5.0,
) -> SolutionValidation:
    interpreter = get_interpreter(language_id)
    cases: list[TestCaseResult] = []

    for index, test in enumerate(problem.tests, start=1):
        result = interpreter.run(code, stdin=test["input"], timeout_seconds=timeout_seconds)
        passed = result.error_type == "ok" and outputs_match_lang(
            test["output"],
            result.stdout,
            language_id=language_id,
        )
        cases.append(
            TestCaseResult(
                index=index,
                stdin=test["input"],
                expected_output=test["output"],
                actual_output=result.stdout,
                error_type=result.error_type,
                stderr=result.stderr,
                passed=passed,
            )
        )

    return SolutionValidation(
        language_id=language_id,
        problem=problem,
        solution_path=solution_path,
        cases=cases,
    )


def validate_solution_path(
    language_id: str,
    problem_id: str,
    *,
    solution_path: Path | None = None,
    solutions_root: Path | None = None,
    dataset_path: Path | None = None,
    timeout_seconds: float = 5.0,
) -> SolutionValidation:
    problem = load_problem(problem_id, dataset_path=dataset_path)
    resolved_path = solution_path or resolve_solution_path(
        language_id,
        problem_id,
        solutions_root=solutions_root,
    )
    code = resolved_path.read_text(encoding="utf-8")
    return validate_solution_code(
        language_id,
        problem,
        code,
        solution_path=resolved_path,
        timeout_seconds=timeout_seconds,
    )


def _escape_text(text: str) -> str:
    return text.encode("unicode_escape").decode("ascii")


def _print_validation(validation: SolutionValidation, *, verbose: bool = False) -> None:
    status = "PASS" if validation.passed else "FAIL"
    print(
        f"{status} {validation.language_id}/{validation.problem.id} "
        f"({validation.passed_tests}/{validation.total_tests}) "
        f"- {validation.problem.title}"
    )
    if validation.solution_path is not None:
        print(f"  solution: {validation.solution_path}")

    if verbose:
        for case in validation.cases:
            case_status = "pass" if case.passed else "fail"
            print(
                f"  case {case.index}: {case_status} "
                f"input='{_escape_text(case.stdin)}' "
                f"expected='{_escape_text(case.expected_output)}' "
                f"actual='{_escape_text(case.actual_output)}' "
                f"error={case.error_type}"
            )
            if case.stderr:
                print(f"    stderr: {_escape_text(case.stderr)}")
        return

    for case in validation.failed_cases:
        print(
            f"  case {case.index} failed: "
            f"input='{_escape_text(case.stdin)}' "
            f"expected='{_escape_text(case.expected_output)}' "
            f"actual='{_escape_text(case.actual_output)}' "
            f"error={case.error_type}"
        )
        if case.stderr:
            print(f"    stderr: {_escape_text(case.stderr)}")


def _validate_all(
    language_id: str,
    *,
    solutions_root: Path,
    dataset_path: Path | None,
    timeout_seconds: float,
    verbose: bool,
) -> int:
    language_dir = solutions_root / language_id
    if not language_dir.is_dir():
        print(f"Missing solutions directory: {language_dir}")
        return 1

    problem_dirs = sorted(path for path in language_dir.iterdir() if path.is_dir())
    if not problem_dirs:
        print(f"No problem directories found in {language_dir}")
        return 1

    validations: list[SolutionValidation] = []
    failures = 0

    for problem_dir in problem_dirs:
        problem_id = problem_dir.name
        try:
            validation = validate_solution_path(
                language_id,
                problem_id,
                solutions_root=solutions_root,
                dataset_path=dataset_path,
                timeout_seconds=timeout_seconds,
            )
        except (FileNotFoundError, ValueError) as exc:
            print(f"FAIL {language_id}/{problem_id} - {exc}")
            failures += 1
            continue
        validations.append(validation)
        _print_validation(validation, verbose=verbose)
        if not validation.passed:
            failures += 1

    total_solutions = len(problem_dirs)
    passed_solutions = sum(1 for validation in validations if validation.passed)
    total_cases = sum(validation.total_tests for validation in validations)
    passed_cases = sum(validation.passed_tests for validation in validations)
    print(
        f"Summary: {passed_solutions}/{total_solutions} solutions passed, "
        f"{passed_cases}/{total_cases} test cases passed."
    )
    return 0 if failures == 0 else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="esolang-test-solution",
        description="Run benchmark test cases against solution files in the solutions directory.",
    )
    parser.add_argument(
        "language",
        choices=sorted(LANGUAGE_METADATA),
        help="Language folder under solutions/ to validate.",
    )
    parser.add_argument(
        "problem_id",
        nargs="?",
        help="Problem id such as E01 or H11. Omit only when using --all.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate every problem directory under solutions/<language>/.",
    )
    parser.add_argument(
        "--solution",
        type=Path,
        help="Explicit solution file path for single-problem validation.",
    )
    parser.add_argument(
        "--solutions-root",
        type=Path,
        default=_default_solutions_root(),
        help="Root directory containing language/problem solution folders.",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=_default_dataset_path(),
        help="Benchmark dataset JSON file to use.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Per-test timeout in seconds.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print every test case, not only failures.",
    )
    return parser


def cli_main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.all and args.solution is not None:
        parser.error("--solution cannot be used with --all")
    if not args.all and not args.problem_id:
        parser.error("problem_id is required unless --all is used")

    if args.all:
        return _validate_all(
            args.language,
            solutions_root=args.solutions_root,
            dataset_path=args.dataset,
            timeout_seconds=args.timeout,
            verbose=args.verbose,
        )

    try:
        validation = validate_solution_path(
            args.language,
            args.problem_id,
            solution_path=args.solution,
            solutions_root=args.solutions_root,
            dataset_path=args.dataset,
            timeout_seconds=args.timeout,
        )
    except (FileNotFoundError, ValueError) as exc:
        print(exc)
        return 1

    _print_validation(validation, verbose=args.verbose)
    return 0 if validation.passed else 1


if __name__ == "__main__":
    raise SystemExit(cli_main())
