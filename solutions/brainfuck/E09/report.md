# E09 - Count Vowels (Brainfuck)

## Approach
Read characters one at a time until EOF. For each character, check if it matches
any of the 10 vowel characters (a, e, i, o, u, A, E, I, O, U) using a flag-based
pattern. If a match is found, increment a counter. After all input is consumed,
convert the counter to decimal digits and output with leading zero suppression.

### Tape Layout
- Cell 0: Input character (preserved across vowel checks)
- Cell 1: Work cell (copy of char for subtraction against each vowel)
- Cell 2: Is-vowel flag (set to 1 when a vowel match is found)
- Cell 3: Temp for zero-check pattern
- Cell 4: Temp for non-destructive copy
- Cell 5: Vowel counter (incremented on each vowel match)
- Cell 6: NUM (copy of counter for division)
- Cell 7: Hundreds digit
- Cell 8: Tens digit
- Cell 9: Ones digit
- Cells 10-15: Temps for divmod operations, copy, and leading zero flag

### Per-Character Algorithm
1. Read a character into cell 0
2. Clear is-vowel flag (cell 2)
3. For each of the 10 vowels:
   a. Copy cell 0 to cell 1 (non-destructive, using cell 4 as temp)
   b. Subtract the vowel's ASCII value from cell 1
   c. Zero-check: set cell 3 = 1; if cell 1 nonzero, clear cell 3; if cell 3
      still 1, set cell 2 = 1 (match found)
4. If cell 2 is 1, increment counter (cell 5)
5. Read next character; loop until EOF (cell 0 = 0)

### Decimal Output
After all input is processed:
1. Copy counter to cell 6
2. divmod(cell 6, 100) -> hundreds digit in cell 7, remainder back to cell 6
3. divmod(cell 6, 10) -> tens digit in cell 8, ones in cell 9
4. Output with leading zero suppression:
   - Hundreds: only if nonzero
   - Tens: only if nonzero or hundreds was output
   - Ones: always output

## Evidence
All 6 test cases pass:
- 'hello' -> '2' (e, o)
- 'Esoteric' -> '4' (E, o, e, i)
- 'xyz' -> '0' (no vowels)
- 'AEIOU' -> '5' (all uppercase vowels)
- 'aaa' -> '3' (three a's)
- 'rhythm' -> '0' (no vowels)

## Difficulties
- Combining two non-trivial BF patterns: vowel checking (10 equality tests)
  and decimal output (divmod with cycling counter). Each is well-understood
  individually, but integrating them requires careful cell layout planning.
- The cycling counter technique for divmod(N, D) is the standard BF approach:
  count down from N, increment a cycle counter; when cycle reaches D, increment
  quotient and reset cycle. The remainder is whatever is left in the cycle counter.
- Leading zero suppression requires a "started output" flag and OR-ing it with
  the current digit value to decide whether to output.

## Difficulty Assessment
Medium. This problem combines two established BF patterns (vowel detection from
M12 and decimal output from E18). Neither pattern is trivial, but both follow
well-known idioms. The main challenge is integrating them with a clean cell layout.

## Design Choices
- Used a flag-based approach for vowel detection: clear flag at start of each
  character, set flag to 1 on any vowel match. This is the same proven approach
  as M12 (Remove Vowels) but inverted (tracking matches instead of non-matches).
- Used cycling counter divmod for decimal conversion, supporting counts 0-255
  (3-digit output). This matches the E18 approach.
- Leading zero suppression with a "started" flag ensures correct output: "0" for
  zero count, no leading zeros for multi-digit counts.

## Assumptions
- EOF returns 0 (confirmed by interpreter behavior).
- Input contains only printable ASCII characters (no embedded null bytes).
- Vowel count fits in a single 8-bit cell (0-255), which is safe since
  input is a single line of text.

## Critique
- The code is long (~3500+ BF instructions) because each of 10 vowel checks
  requires a full copy-subtract-zero-check sequence, and the decimal output
  routine is verbose.
- A more compact approach could use arithmetic tricks (e.g., case-insensitive
  check by OR-ing with 32, then checking just 5 lowercase vowels), but the
  straightforward approach is more reliable and easier to verify.
- The divmod is done twice (for hundreds and tens), duplicating code. A loop
  could reduce this but would require more complex cell management.
