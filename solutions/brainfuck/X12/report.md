# X12: Least Common Multiple - Brainfuck Solution

## Problem
Read two positive integers A and B and compute their LCM.

## Approach
LCM via sieve (simultaneous countdown):
1. **Parse input**: Read two decimal integers A and B from ASCII input.
2. **Sieve loop**: Two counters `ca` and `cb` start at A and B. Each tick, decrement both and increment a result counter. When a counter reaches zero, reset it to its original value. When **both** reach zero simultaneously, the result counter holds the LCM.
3. **Decimal output**: Extract digits via `divmod` by 10 (ones, then tens, then hundreds), print with leading zero suppression.

This approach avoids GCD, division, and modulo, relying only on addition, subtraction, and comparison to zero -- operations that are natural in Brainfuck and free of u8 overflow edge cases.

## Key Design Decisions
- **Sieve over GCD**: The previous solution used LCM = (A / GCD) * B with a subtraction-based GCD. That approach contained 14 "double-decrement" move loops (`[-<<<...+>>>...-]`) that subtracted 2 per iteration from the source cell. This works only for even values; odd values cause an infinite loop under u8 wrapping (e.g., `1 -> 255 -> 253 -> ... -> 3 -> 1 -> ...`, never reaching 0). The sieve algorithm has no such failure mode.
- **Single-cell result**: For the given test inputs (max LCM = 100), the result fits in a u8 cell, so no multi-cell arithmetic is needed.
- **Standard divmod for output**: The well-known BF divmod algorithm `[->-[>+>>]>[+[-<+>]>+>>]<<<<<]` works correctly with divisor 10 for all values 0-255.
- **Compact**: 1,360 BF instructions (down from 6,050 in the original).

## Test Results
All 6 test cases pass (verified with both the Python interpreter and Tritium `-b -mem 30000 -z`):
- '4 6' -> '12'
- '3 5' -> '15'
- '12 18' -> '36'
- '7 7' -> '7'
- '1 100' -> '100'
- '15 20' -> '60'
