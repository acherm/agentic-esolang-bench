# Agentic Replication of EsoLang-Bench: 100% on Brainfuck

This repository is an **independent replication** of [EsoLang-Bench](https://github.com/Lossfunk/EsolangBench) ([paper](https://arxiv.org/abs/2603.09678)), a benchmark that tests LLMs on code generation in esoteric programming languages.

The original paper reports that the best frontier model (GPT-5.2) achieves **3.8%** overall, and the best agentic result on Brainfuck is **13.8%** (Codex). We used **Claude Code** (Claude Opus 4.6, agentic mode, 1M context) and achieved **100% on Brainfuck** -- solving all 80 problems across all four difficulty tiers.

## Results

| Difficulty | Score | Example problems |
|---|---|---|
| Easy | **20/20** | Hello World, reverse string, sum two integers, even/odd |
| Medium | **20/20** | Palindrome check, GCD, Fibonacci, bubble sort, Caesar cipher |
| Hard | **20/20** | Balanced parentheses, big integer addition, prime counting, expression evaluation |
| Extra Hard | **20/20** | Postfix evaluation, matrix multiplication, Roman numeral conversion, Josephus problem |

### Context: original paper results

| Model | Strategy | Brainfuck Accuracy |
|---|---|---|
| GPT-5.2 | Self-Scaffolding | 3.8% |
| Codex (Agentic) | -- | 13.8% |
| Claude Code | -- | 12.5% |
| **This replication (Claude Code, Opus 4.6)** | **BF-as-compilation-target** | **100%** |

## How it works

The key insight is treating Brainfuck as a **compilation target**, not a language to write by hand.

1. **Python generator**: A `BFGen` framework provides high-level primitives -- `move_to(cell)`, `copy(src, dst, tmp)`, `add_const(cell, n)`, decimal I/O routines, comparison, arithmetic. The agent writes Python that emits BF.
2. **Local validation**: Each generated BF program is tested against all 6 spec tests using the repository's built-in `BrainfuckInterpreter` before being accepted.
3. **Agentic loop**: Claude Code iterates -- generating, testing, debugging, and retrying -- until all tests pass. No manual intervention.

All 80 solutions (`.bf` programs + reports with approach, evidence, design choices, and difficulty assessment) are in [`solutions/brainfuck/`](solutions/brainfuck/).

## Reproducing

This repo is a fork of [Lossfunk/EsolangBench](https://github.com/Lossfunk/EsolangBench). The original benchmark code, interpreters, and problem definitions are unchanged. Only `solutions/` was added.

```bash
pip install -e .
```

To verify a solution against the interpreter:

```python
from esolang_bench import get_interpreter

interp = get_interpreter("brainfuck")
code = open("solutions/brainfuck/H11/solution.bf").read()
result = interp.run(code, stdin="a3b2")
print(result.stdout)  # "aaabb"
```

## Citation

Original benchmark:

```bibtex
@article{sharma2026esolangbench,
  title={{EsoLang-Bench}: Evaluating Genuine Reasoning in Large Language Models
         via Esoteric Programming Languages},
  author={Sharma, Aman and Chopra, Paras},
  journal={arXiv preprint arXiv:2603.09678},
  year={2026},
  url={https://arxiv.org/abs/2603.09678}
}
```

This replication:

```bibtex
@misc{acher2026esolangbench-replication,
  title={Agentic Replication of {EsoLang-Bench}: 100\% on Brainfuck
         with Claude Code},
  author={Acher, Mathieu},
  year={2026},
  url={https://github.com/acherm/agentic-esolang-bench}
}
```

## License

Code: [MIT](LICENSE) | Dataset: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
