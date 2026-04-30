from esolang_bench.solution_tester import (
    cli_main,
    load_problem,
    resolve_solution_path,
    validate_solution_code,
    validate_solution_path,
)


def test_resolve_solution_path_finds_repo_solution():
    path = resolve_solution_path("brainfuck", "E01")
    assert path.name == "solution.bf"
    assert path.is_file()


def test_validate_solution_path_passes_real_solution():
    validation = validate_solution_path("brainfuck", "E01", timeout_seconds=1.0)
    assert validation.passed
    assert validation.passed_tests == 6


def test_validate_solution_code_reports_failures():
    problem = load_problem("E01")
    validation = validate_solution_code("brainfuck", problem, "+.", timeout_seconds=1.0)
    assert not validation.passed
    assert validation.passed_tests == 0
    assert len(validation.failed_cases) == 6


def test_cli_main_returns_zero_for_passing_solution(capsys):
    exit_code = cli_main(["brainfuck", "E01", "--timeout", "1"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "PASS brainfuck/E01" in captured.out
