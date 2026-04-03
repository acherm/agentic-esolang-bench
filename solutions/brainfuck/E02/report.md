# E02 — Echo Line (Brainfuck)

## Approach
Simple read-print loop using the classic BF idiom `,[.,]`.

The algorithm:
1. Read the first character into cell 0 (`,`).
2. Enter a loop conditioned on the cell being nonzero (`[`).
3. Print the current character (`.`).
4. Read the next character (`,`).
5. If the character is nonzero (not EOF), repeat; otherwise exit the loop (`]`).

This relies on the BF convention that `,` returns 0 on EOF (end of input).

## Evidence (Test Results)
All 6 spec tests pass:
- "Hello" → "Hello"
- "abc123" → "abc123"
- "Brainfuck is fun" → "Brainfuck is fun"
- "X" → "X"
- "!@#$%^&*()" → "!@#$%^&*()"
- "   spaces   " → "   spaces   "

The program correctly preserves all characters including spaces, punctuation,
digits, and special characters.

## Difficulties
None. This is the canonical introductory BF problem. The `,[.,]` idiom is
one of the most fundamental BF patterns and directly solves the echo task.

## Difficulty Assessment
**Trivial** — This is the simplest possible I/O problem in Brainfuck.
The solution is a single well-known idiom that every BF programmer learns
first.

## Design Choices
- Used a single cell (cell 0) since no buffering or transformation is needed.
- No special handling for newlines — the problem says to echo back exactly,
  and the test inputs contain no trailing newlines.
- Relied on EOF returning 0, which is the behavior of this benchmark's
  interpreter (confirmed by reading the interpreter source).

## Assumptions
- The BF interpreter returns 0 on EOF for the `,` command. This is confirmed
  by the EsolangBench BrainfuckInterpreter source code (line 65:
  `tape[pointer] = input_queue.popleft() if input_queue else 0`).
- Input does not contain null bytes (ASCII 0), which would prematurely
  terminate the loop. This is a safe assumption for text input.

## Critique of the Problem
The problem is well-defined and straightforward. It serves as a good
introductory exercise for any esolang. The test cases cover a reasonable
variety of inputs: letters, digits, special characters, spaces, and
varying lengths. One could argue that an empty-input test case would
strengthen the suite (the program handles it correctly — it reads 0
immediately and produces no output), but the existing tests are sufficient.
