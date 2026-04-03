# E05: Multiply Two Integers - Brainfuck Solution

## Approach
Parse two signed integers from input, multiply using repeated addition
with a decimal digit array accumulator, and output the result.

1. **Parsing**: Read each character, detect optional minus sign, accumulate
   decimal digits into a byte value (ABS_A, ABS_B) using multiply-by-10-and-add.
   First number terminated by space, second by newline/EOF.

2. **Sign handling**: Track signs separately. Result sign = XOR of input signs
   (implemented as addition mod 2). If result is zero, no sign is printed.

3. **Multiplication**: Outer loop runs ABS_B times. Inner loop adds ABS_A
   ones to a 6-digit decimal accumulator with carry propagation at each
   digit position.

4. **Output**: Leading zero suppression using a "started" flag. Digits
   printed from most significant to least significant, each converted
   to ASCII by adding 48.

## Key Design Choices
- 6-digit decimal accumulator (range 0-999999) for the product
- Byte-sized operands (0-255) parsed from multi-digit decimal input
- Repeated addition for multiplication (simple, correct for small inputs)
- Carry check at each digit: compare to 10, if equal set to 0 and carry
- Separate zero-result handling to avoid printing "-0"

## Evidence
All 6 provided test cases pass:
- 3 * 4 = 12 (basic multiplication)
- -2 * 5 = -10 (negative * positive)
- 7 * 0 = 0 (zero product)
- 11 * 11 = 121 (two-digit * two-digit)
- -3 * -4 = 12 (negative * negative = positive)
- 25 * 4 = 100 (product with trailing zeros)

## Difficulties
- **8-bit cell overflow**: Cannot store products > 255 in a single cell.
  Solved by using a decimal digit array with per-digit carry propagation.
- **Carry detection**: Checking if a digit equals 10 requires a non-destructive
  comparison (copy, subtract, check zero) since the digit must be preserved
  if no carry occurs.
- **Input termination**: Second number can end with newline, CR, or EOF.
  Used multi-check approach testing for each possible terminator.
- **Zero product sign**: Must not print "-0" when result is zero with
  negative sign. Handled by checking all digits before sign output.
- **Leading zero suppression**: Required a "started printing" flag that
  activates on first nonzero digit and forces printing of all subsequent
  digits (including internal zeros like in "100").

## Difficulty Assessment
Medium. The core multiplication algorithm (repeated addition) is simple,
but the surrounding infrastructure (multi-digit decimal parsing, decimal
accumulator with carry, leading zero suppression, sign handling) requires
careful BF programming. The 8-bit cell limitation forces the decimal
digit array approach, adding complexity.

## Assumptions
- Input numbers fit in a byte (0-255 absolute value)
- Products fit in 6 decimal digits (up to 999999)
- Input format: two integers separated by single space
- EOF returns 0 from the interpreter
- Numbers consist of optional minus sign followed by decimal digits

## Critique
The repeated addition approach has O(A*B) time complexity, which could be
slow for larger inputs (worst case 255*255 = 65025 additions, each with
carry propagation). For the given test cases with small numbers, this is
fast enough. A grade-school long multiplication algorithm on digit arrays
would be O(d_A * d_B) where d is digit count, but would be much more
complex to implement in BF. The current approach trades computational
efficiency for implementation simplicity.

Code length could be reduced by using more compact BF patterns for
comparison and carry detection, but correctness and clarity were
prioritized over code golf.
