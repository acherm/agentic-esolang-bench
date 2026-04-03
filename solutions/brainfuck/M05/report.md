# M05: Simple Binary Expression (Brainfuck)

## Problem
Read "a op b" where a,b are integers and op is +, -, or *.
Output the integer result.

## Approach
- **Representation**: 7-digit decimal arrays (ones to millions, supporting values up to 9,999,999).
- **Input parsing**: Read optional minus sign, then digits left-to-right with shift-and-store.
- **Subtraction**: Convert to addition by flipping B's sign, then dispatch on same vs different sign.
- **Same-sign addition**: Digit-by-digit add with divmod10 carry propagation.
- **Different-sign subtraction**: Try A-B with add-10-then-divmod10 borrow detection. If outstanding borrow, recompute as B-A.
- **Multiplication**: Long multiplication (unrolled nested loops over digit pairs) with divmod10 carry propagation.
- **Output**: Skip leading zeros, print minus for negative, special-case zero.
- **Key BF technique**: divmod10 uses copy-then-check (not direct check) to avoid destroying the countdown cell.

## Code size
39483 characters of Brainfuck.
