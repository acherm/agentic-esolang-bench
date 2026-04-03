# Prompts used to solve EsoLang-Bench in Brainfuck

This document records the exact prompts given to Claude Code (Claude Opus 4.6, 1M context) during the agentic session that produced the 80 Brainfuck solutions.

## Tool and setup

- **Tool**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (CLI, agentic mode)
- **Model**: Claude Opus 4.6 with 1M token context window
- **Working directory**: a local clone of [Lossfunk/EsolangBench](https://github.com/Lossfunk/EsolangBench)
- **No manual code edits**: all solutions were generated, tested, and saved by Claude Code autonomously. The only human inputs were the prompts below and "retry/continue" when subagents hit rate limits.

## Prompt 1: First problem (H11) with working rules

The first problem was given with detailed instructions that established the methodology for the entire session:

```
Solve one EsoLang-Bench problem in Brainfuck.

Use tools if available. Validate against the local interpreter before finishing.

Problem ID: H11
Title: Run Length Decoding
Difficulty: hard

Description:
Read a run-length encoded string consisting of alternating characters and single-digit
counts (1-9), for example `a3b2`.
Decode it by repeating each character count times and output the expanded string.

Specification tests (stdin => stdout):
1. Input: a3b2       Output: aaabb
2. Input: x1         Output: x
3. Input: z9         Output: zzzzzzzzz
4. Input: A2B3C1     Output: AABBBC
5. Input: m4n2p1     Output: mmmmnnp
6. Input: q1w1e1r1   Output: qwer

Important working rules:

1. Do not hand-write Brainfuck except for tiny probes.
   Treat Brainfuck as a compilation target. Build a generator script and emit BF from it.

2. Work in /tmp only.
   Do not modify repository source files.

3. Build a small helper layer in the generator:
   - move_to(cell)
   - clear(cell)
   - add_const(cell, n)
   - copy(src, dst, tmp)
   - move_value(src, dst)
   - emit_char_from_cell(cell)
   - read_char_to_cell(cell)

4. Keep a fixed tape layout and document it in the generator.
   Name each cell/block by purpose. Avoid implicit pointer reasoning.

5. Put execution next to generation.
   Define a `bf_run(code, stdin)` helper or call the local interpreter from the same script.
   Test after every change. Do not reason about correctness from the BF source alone.

6. Optimize for correctness, not compactness.
   A long BF program is acceptable.

7. Solve this with a streaming parser.
   Read one symbol, then one digit, convert the digit from ASCII to an integer 1-9,
   emit the symbol that many times, then continue until EOF.

8. Avoid unnecessary generality.
   Counts are single decimal digits only. You do not need multi-digit parsing or
   arithmetic beyond decrementing a small counter.

9. Add a few extra tests before finalizing.
   Include at least: a single pair, multiple pairs, count 1, count 9.

10. Final response format:
    Write the final Brainfuck program to /tmp/final.bf.
    In your final response, return only the absolute path /tmp/final.bf.
```

## Prompt 2: Solve all remaining problems

After H11 was solved and validated, the following prompt launched the batch solve of the remaining 79 problems:

```
it was problem H11... please address other problems in Brainfuck, in the order you want
(first try with problems you consider "easy")... save solutions in a dedicated subfolder
of a folder "solutions", and for each problem write a report including approach, evidence,
difficulties, assessment of the difficulty, critics of the problem, design choices,
assumptions, etc.)
```

## Subsequent prompts

The only other human inputs during the session were:

- `retry/continue` (repeated ~5 times) -- when subagents hit API rate limits or timed out, this resumed the batch processing
- `please commit` -- to create the git commit
- `git push agentic-esolang-bench on Github (repo to be created)` -- to publish

## What Claude Code did autonomously

From these prompts, Claude Code:

1. **Explored the repository** to find all 80 problem definitions, the interpreter, and test cases
2. **Built a reusable framework** (`/tmp/bf_framework.py`) with `BFGen` helpers, test runner, and problem loader
3. **Solved problems in batches of 6**, parallelizing subagents by difficulty tier (easy first, then medium, hard, extra hard)
4. **For each problem**: read the spec, designed an algorithm, wrote a Python generator, tested against all 6 spec tests + extra edge cases, saved the `.bf` and `report.md`
5. **Iterated on failures**: when solutions failed tests, the agent debugged and retried (sometimes through multiple iterations)
6. **Developed reusable patterns** across problems: decimal I/O routines, comparison via simultaneous decrement, shuttle-based indexed access, 10s complement arithmetic, etc.

The entire session (all 80 problems) ran in a single Claude Code conversation over ~2 days, with rate-limit pauses.
