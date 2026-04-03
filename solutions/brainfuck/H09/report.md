# H09: General Caesar Cipher (Brainfuck)

## Problem
Read integer K (possibly negative) and lowercase string S.
Shift each character by K positions mod 26, output result.

## Approach
1. Parse integer K from input (handle negative sign and multi-digit)
2. Compute K mod 26 using repeated subtraction with dual-decrement comparison
3. If K was negative, convert to positive equivalent: K_eff = (26 - K) mod 26
4. For each character: subtract 'a', add K, mod 26 (single subtraction since max is 50), add 'a' back, output

## Tape Layout
- Cell 0: sign flag
- Cell 1: K value
- Cell 2: current char / offset
- Cells 3-9: temporaries for comparison and arithmetic
- Cell 10: K copy for repeated use

## Code length
1514 characters
