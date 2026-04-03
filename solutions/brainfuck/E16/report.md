# E16: First And Last Character - Brainfuck Solution

## Approach
Read the first character, copy it as a default "last" character, then read
remaining characters one by one (overwriting the "last" cell each time).
Finally print: first char, space, last char.

## Tape Layout
- Cell 0: first character (read once, printed immediately)
- Cell 1: last character (initialized as copy of first; overwritten by each subsequent char)
- Cell 2: temp cell for reading next characters
- Cell 3: scratch cell for copy operations and printing space

## Algorithm Detail
1. Read first char into cell 0
2. Copy cell 0 to cell 1 using cell 3 as temp (handles single-char case)
3. Print cell 0
4. Set cell 3 to 32 (ASCII space) and print it
5. Read into cell 2; loop while cell 2 is nonzero:
   - Clear cell 1, move cell 2 into cell 1
   - Read next char into cell 2
6. Print cell 1 (the last character read, or the first if only one char)

## Evidence
All 6 spec tests pass, plus 5 single-char edge cases
and 5 additional edge cases.

## Difficulties
The main challenge is handling the single-character case where first = last.
Solved by copying the first character into the "last" cell before the read loop,
so if no additional characters are read, the first character serves as the last.

## Difficulty Assessment
Low-medium. The logic is straightforward once you decide on the tape layout
and handle the single-char edge case. The BF implementation mainly requires
a copy operation and a simple read loop.

## Design Choices
- Used a destructive move (move_value) instead of copy for transferring each
  new character to the "last" cell, since we don't need to preserve it in the
  temp cell (it gets overwritten by the next read anyway).
- Pre-copied first char to last cell rather than adding a conditional check
  for EOF after the loop.

## Assumptions
- EOF returns 0 (standard BF behavior), which terminates the read loop.
- Input contains at least one character (guaranteed by problem statement).
- Input is a single line with no trailing newline in the test data.

## Critique
The solution is clean and minimal. The copy operation at the start adds some
code length but is necessary for correctness on single-character inputs.
An alternative would be to check after the loop whether any characters were
read, but that would require more complex conditional logic in BF.

## Code Size
98 characters of Brainfuck.
