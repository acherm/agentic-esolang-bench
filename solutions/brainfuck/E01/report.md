# E01 — Print Hello World (Brainfuck)

## Approach

Used the `BFGen.print_string()` helper to generate a Brainfuck program that
prints the string "Hello World!" character by character. The method works by:

1. Clearing a single cell (cell 0) at the start.
2. For each character in the target string, computing the difference between
   its ASCII value and the current cell value, then emitting `+` or `-`
   instructions to adjust the cell to the target value, followed by `.` to
   output the character.

This incremental approach is more efficient than setting each character's
ASCII value from zero, because consecutive characters often have similar
ASCII codes (e.g., 'l' and 'o' differ by only 3).

## Evidence (Test Results)

All 6 specification tests passed:
- Each test provides empty input and expects "Hello World!" as output.
- The interpreter returned the exact expected string in every case.

Generated program length: 368 characters.

## Difficulties

None. This is the simplest possible Brainfuck problem — pure output with
no input, no conditionals, and no loops. The `print_string()` utility
handles all the character encoding automatically.

## Difficulty Assessment

**Easy.** This is universally considered the canonical introductory problem
for any programming language. In Brainfuck it requires only `+`, `-`, and
`.` instructions (no `,`, `[`, or `]`). The main challenge in Brainfuck is
managing ASCII values efficiently, but `print_string()` handles that with
its incremental delta approach.

## Design Choices

- **Single-cell approach:** The entire string is printed using only cell 0.
  No additional cells are needed because there is no input to read and no
  computation to perform — just sequential output.
- **Incremental deltas:** Rather than resetting the cell to zero before each
  character, the generator computes the signed difference between consecutive
  characters. For "Hello World!" the ASCII values are [72, 101, 108, 108, 111,
  32, 87, 111, 114, 108, 100, 33], and the deltas between them are relatively
  small, saving many instructions compared to a naive absolute-value approach.
- **No loop-based multiplication:** A more advanced approach would use a
  multiply loop (e.g., `+++++++++[>++++++++<-]>.`) to set large values with
  fewer instructions. This was not needed here because code size is not a
  constraint and the incremental approach is already reasonably compact.

## Assumptions

- The output must be exactly "Hello World!" with no trailing newline, as
  specified by the problem description and confirmed by the test cases.
- The Brainfuck interpreter uses 8-bit wrapping cells (standard), though
  this problem only uses values 32–114 so cell size is irrelevant.

## Critique of the Problem

This problem serves as a good warm-up and sanity check for any Brainfuck
toolchain, but it tests essentially nothing beyond the ability to emit
constant output. A slightly more interesting variant would ask for
"Hello, <name>!" which requires reading input — that is covered by E03.

## Generated Code

```brainfuck
[-]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.-------------------------------------------------------------------------------.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.------.--------.-------------------------------------------------------------------.
```
