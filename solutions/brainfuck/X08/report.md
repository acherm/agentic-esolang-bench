# X08: Count Set Bits In Range - Brainfuck Solution

## Problem
Read two integers L and R, count total 1-bits in binary representations of all integers from L to R inclusive.

## Algorithm
1. Parse L and R from decimal ASCII input
2. For each number from L to R:
   - Compute popcount using repeated divide-by-2 with toggle (8 iterations for 8-bit numbers)
   - Add popcount to 16-bit total (low byte + high byte with carry detection)
3. Convert 16-bit total to BCD (4 decimal digits)
4. Output decimal result with leading zero suppression

## Key Implementation Details
- Decimal parsing: multiply-by-10-and-add loop, space-delimited
- Division by 2: toggle pattern (alternate remainder 0/1 while counting quotient)
- 16-bit addition: increment low byte, detect wrap-to-zero for carry to high byte
- BCD conversion: increment ones digit with carry chain through tens, hundreds, thousands
- THI*256 to BCD: nested 16x16 loop for 256 increments per high byte unit
- Output: skip leading zeros, always print at least ones digit
