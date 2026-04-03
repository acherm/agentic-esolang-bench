# H04 - Nth Prime Number (Brainfuck)

## Problem
Read K >= 1 and output the Kth prime number (1-indexed: 2, 3, 5, 7, 11, ...).

## Algorithm
1. Parse multi-digit decimal input into K.
2. Starting from candidate=2, test each candidate for primality via trial division.
3. For each prime found, decrement K. When K reaches 0, output that prime.
4. Output the result as a decimal string with leading zero suppression.

## Implementation Details
- Input parsing: Handles multi-digit decimal numbers, terminates on newline or EOF.
- Primality test: Trial division testing divisors from 2 to candidate-1.
  Uses counting modulo (O(n) per modulo) which is efficient for small candidates.
- Decimal output: Divmod by 100 then by 10 to extract digits, with leading zero suppression.
- Single-byte arithmetic sufficient (max prime 251 for K up to 54).

## Code size
2799 characters of Brainfuck.
