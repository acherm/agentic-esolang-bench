# X16: Hamming Distance - Brainfuck Solution

## Problem
Read two non-negative integers A and B. Compute the Hamming distance between
their binary representations (number of bit positions where they differ) and
output that count.

## Approach
1. Parse two decimal integers from input (A and B)
2. For each of 8 bit positions:
   - Extract LSB of A (A mod 2) and LSB of B (B mod 2) using divmod-by-2
   - XOR the two bits using toggle technique
   - Add XOR result to hamming distance counter
   - Replace A and B with their respective quotients (A/2, B/2)
3. Output the counter as a single ASCII digit (max value is 8)

## Memory Layout
- c0: A (working value, halved each iteration)
- c1: B (working value, halved each iteration)
- c2: Hamming distance counter
- c3: Bit loop counter (8 iterations)
- c4-c8: Temporary workspace for divmod and XOR operations
- c10-c14: Input parsing workspace
