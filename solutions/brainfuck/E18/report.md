# E18: Count Spaces - Brainfuck Solution

## Approach
Read characters one at a time until EOF (which returns 0 in this interpreter).
For each character, compare it to ASCII 32 (space) using subtraction and a
zero-check flag pattern. If the character is a space, increment a counter.

After processing all input, convert the counter to decimal digits using
repeated division by 10 (via a cycling counter technique), then output
the digits with leading zero suppression.

## Evidence
All spec tests pass:
- "hello world" -> "1"
- "no_spaces_here" -> "0"
- "a b c" -> "2"
- "   " -> "3"
- "one two three four" -> "3"
- "x" -> "0"

## Cell Layout
- Cell 0: input character
- Cell 1: space counter
- Cell 2-5: temps for comparison (copy, subtract 32, flag check)
- Cell 6: NUM (copy of counter for division)
- Cell 7: tens digit
- Cell 8: ones digit
- Cell 9-14: temps for division and digit extraction
- Cell 15: "started output" flag for leading zero suppression

## Key Techniques
1. **EOF detection**: The interpreter returns 0 on EOF, so the main read loop
   naturally terminates.
2. **Equality check**: Copy char, subtract 32, use flag pattern (set flag=1,
   if nonzero clear flag) to detect zero result.
3. **Decimal conversion**: Cycle counter mod 10 approach - count down from N,
   incrementing a cycle counter; each time it reaches 10, increment quotient
   and reset cycle counter. Remainder stays in cycle counter.
4. **Leading zero suppression**: Track whether any digit has been output yet;
   skip tens/hundreds digit if zero and nothing output before it.

## Difficulties
- Decimal output is the hardest part. BF has no division instruction, so we
  must implement divmod(N, 10) manually using repeated subtraction with a
  cycling counter.
- Leading zero suppression requires careful flag management to avoid outputting
  "03" instead of "3" while still outputting "0" for zero count.
- Non-destructive comparison requires copy operations with temp cells.

## Difficulty Assessment
Medium. The character comparison loop is straightforward BF, but the decimal
output routine adds significant complexity. The cycling-counter divmod technique
and leading zero suppression each require multiple cells and careful flag logic.

## Design Choices
- Used cycling counter for divmod rather than repeated subtraction with
  underflow detection, since BF cells wrap around (8-bit unsigned).
- Supports counts up to 255 (3-digit output) for robustness, though test
  cases only need counts up to ~18.
- Each "if-zero" check uses the standard flag pattern: set flag=1, loop on
  the value to clear flag if nonzero, then check flag.

## Assumptions
- EOF returns 0 (verified with interpreter).
- Input contains no null bytes (standard assumption).
- 8-bit wrapping cells (standard BF).
- Counts fit in a single cell (0-255), which is safe since input is "a line
  of text" (max ~255 chars, and all being spaces would give count 255).

## Critique
- The generated code is long (~2000+ BF instructions) due to the decimal
  output routine. A more compact approach might use hardcoded lookup tables
  or exploit BF tricks for shorter code.
- The division is done twice (for hundreds and tens), duplicating code. A
  subroutine-like pattern could reduce this, but BF lacks functions.
- The solution handles up to 255 correctly, which exceeds requirements but
  adds robustness.
