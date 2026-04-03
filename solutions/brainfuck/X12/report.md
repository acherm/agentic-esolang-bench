# X12: Least Common Multiple - Brainfuck Solution

## Problem
Read two positive integers A and B and compute their LCM.

## Approach
LCM(A, B) = (A / GCD(A, B)) * B

1. **Parse input**: Read two decimal integers A and B from ASCII input separated by a space.
2. **Copy A and B** for GCD computation.
3. **GCD by subtraction**: Repeatedly subtract the smaller from the larger until both are equal. Uses simultaneous decrement of copies to determine which is larger, then subtracts accordingly.
4. **Exact division A / GCD**: Since GCD divides A, repeated subtraction of GCD from A gives the exact quotient.
5. **Multiply quotient * B in decimal**: Increment a 5-digit decimal accumulator (ones through ten-thousands) a total of quotient * B times. Each increment adds 1 to the ones digit and propagates carries through all digit positions.
6. **Output with leading zero suppression**: Print digits from most significant to least significant, skipping leading zeros. The ones digit is always printed.

## Key Design Decisions
- Used decimal digit array (5 cells, one per digit) to avoid multi-byte binary arithmetic and base conversion.
- GCD uses subtract-smaller-from-larger with simultaneous decrement for comparison, avoiding the need for division/modulo.
- Division A/GCD uses simple repeated subtraction since the division is exact.
- Multiplication uses nested loops (quotient iterations x B iterations) with single-increment decimal accumulation, keeping carry logic simple.

## Test Results
All 6 test cases pass:
- '4 6' -> '12'
- '3 5' -> '15'
- '12 18' -> '36'
- '7 7' -> '7'
- '1 100' -> '100'
- '15 20' -> '60'
