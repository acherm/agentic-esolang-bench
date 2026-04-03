# H13: Polynomial Evaluation (Brainfuck)

## Problem
Read integer n, then n+1 coefficients (highest-degree first), then x.
Evaluate the polynomial at x using Horner's method and output the result.

## Approach
- **Representation**: Signed 7-digit decimal arrays (sign + ones to millions, up to 9,999,999).
- **Input parsing**: Skip whitespace, detect minus sign, shift-and-store digits.
- **Coefficient storage**: Unrolled loop stores up to 11 coefficients at fixed tape positions.
- **Horner's method**: Unrolled conditional loop; each step multiplies RESULT by X, XORs signs, adds next coefficient.
- **Multiplication**: Long multiplication over digit pairs with divmod10 carry propagation.
- **Signed addition**: Dispatch on same/different sign; same -> add magnitudes, different -> subtract with borrow detection.
- **Output**: Skip leading zeros, print minus for negative, special-case zero.

## Code size
1143911 characters of Brainfuck.
