# H12 - ASCII Sum (Brainfuck)

## Approach
Decimal accumulator with 5 digit cells (ones, tens, hundreds, thousands, ten-thousands)
supporting sums up to 99999.

For each input character:
1. Add its ASCII value to the ones digit cell
2. Perform divmod-by-10 on each digit position, propagating carries upward

The divmod-by-10 is implemented with a cycling counter: decrement the value while
incrementing a counter. When the counter reaches 10, reset it and increment the quotient.
The remainder is left in the counter.

Output uses leading-zero suppression: skip leading zeros for higher digit positions,
always print the ones digit.

## Evidence
All 6 test cases pass:
- 'A' -> '65' (single character)
- 'AB' -> '131' (two characters)
- 'abc' -> '294' (three characters)
- 'a' -> '97' (single lowercase)
- 'Hello' -> '500' (five characters, sum exactly 500)
- '123' -> '150' (digit characters)

## Difficulties
- BF cells are 8-bit (0-255), so multi-character ASCII sums easily overflow a single cell
- Divmod by 10 in BF requires careful implementation with counter cycling and flag-based
  conditional logic
- Leading zero suppression for output requires tracking whether any non-zero digit has
  been printed

## Difficulty Assessment
Hard. This problem requires:
- Multi-precision decimal arithmetic in BF
- Divmod operation (non-trivial in BF)
- Conditional output with leading zero suppression
- Multiple interacting subsystems (accumulator, carry propagation, output formatting)

## Design Choices
- 5 decimal digit cells support sums up to 99999, sufficient for any reasonable input
- Decimal representation avoids binary-to-decimal conversion at output time
- Carry propagation after each character addition (not deferred) keeps digit values bounded
- The divmod10 uses a simple counter approach: count up to 10, reset and increment quotient

## Assumptions
- Input consists of printable ASCII characters (values 32-126)
- Input is terminated by EOF (BF reads 0 on EOF)
- Sum fits in 5 decimal digits (up to 99999)
- BF uses 8-bit wrapping cells

## Critique
- The code is long due to repeated divmod10 calls for each digit position
- Each divmod10 expansion uses 5 scratch cells and involves multiple copy operations
- A more compact approach might use cell-pair binary arithmetic, but decimal representation
  simplifies the output phase considerably
- The solution trades code size for correctness and clarity of approach
