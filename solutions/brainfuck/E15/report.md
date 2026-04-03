# E15 — Concatenate Two Lines (Brainfuck)

## Approach
Read and echo the first line character by character until a newline (ASCII 10) is detected,
then output a space (ASCII 32), then echo the second line until EOF.

Newline detection uses subtract-10-and-check: read a char, subtract 10, and enter a loop.
If the result is zero (was newline), the loop is skipped. If nonzero, add 10 back to restore
the original character, output it, read the next char, subtract 10, and repeat.

## Evidence
All 6 test cases pass, including single-character lines ("a" + "b") and numeric lines.

## Difficulties
None significant. The main subtlety is correctly detecting newline by subtracting 10 before
the loop condition check and restoring the value inside the loop.

## Difficulty Assessment
Easy. This is a straightforward character-by-character I/O problem with a single delimiter check.

## Design Choices
- Single-cell tape layout (cell 0 only) — no need for additional cells since we process
  one character at a time with no storage requirements.
- Subtract-and-check pattern for newline detection avoids needing comparison or flag cells.

## Assumptions
- Input always contains exactly one newline separating two non-empty lines.
- EOF returns 0 (standard BF convention used by the interpreter).
- No newline characters appear within S1 or S2 themselves.
- Input characters are all in the printable ASCII range (none equal to ASCII 10 except the delimiter).

## Critique
The solution is minimal and efficient. The subtract-10 approach would fail if any input
character happened to have ASCII value 10 within a line, but the problem guarantees the
only newline is the line separator. A more robust approach could use a flag cell, but that
would be unnecessary complexity for this problem specification.
