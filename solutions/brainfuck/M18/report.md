# M18: Sum Of List - Brainfuck Solution

## Approach
Decimal digit array (7 digits) with 10s complement arithmetic.

1. Parse N from first line as a binary value.
2. Loop N times:
   - Skip whitespace, parse optional sign and digits.
   - Store number in 7 decimal digit cells.
   - Convert negative numbers to 10s complement.
   - Add to accumulator digit-by-digit with carry propagation.
3. Output:
   - Detect negative (top digit >= 5), output '-' and convert back.
   - Print digits with leading zero suppression.

## Key Design Choices
- 7-digit decimal representation (range: -5000000 to 4999999)
- 10s complement for negatives eliminates separate add/subtract logic
- Carry detection via parallel countdown comparison
- Leading zero suppression in output

## Evidence
All 6 test cases pass.

## Code size
15018 characters
