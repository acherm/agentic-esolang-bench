# H02 - Evaluate Expression With Precedence (Brainfuck)

## Algorithm
Two-accumulator approach for operator precedence without parentheses:
- `add_acc`: running total of addition/subtraction results
- `mul_acc`: current multiplication chain accumulator
- `pending_op`: pending +/- operator (0 = add, 1 = subtract)
- `first_mul`: flag indicating next number starts a new multiplication chain

Processing:
1. Parse digits into multi-digit numbers (num = num * 10 + digit)
2. On `*`: process current number into mul_acc (set or multiply), continue chain
3. On `+` or `-`: process number, flush mul_acc to add_acc using pending_op, reset chain
4. On EOF: process last number, final flush to add_acc, output result

This correctly handles `*` before `+`/`-` precedence with left-to-right evaluation.

## Tape Layout
- Cell 0: add_acc (running sum)
- Cell 1: pending_op (0=add, 1=subtract)
- Cell 2: mul_acc (multiplication chain)
- Cell 3: first_mul flag
- Cell 4: current number being parsed
- Cell 5: current input character
- Cell 6: main loop flag
- Cell 7: handled flag
- Cells 8-18: temporaries for arithmetic and conditionals
- Cells 20-31: output workspace (divmod by 10 for decimal conversion)

## Output
Uses the standard BF divmod algorithm `[->-[>+>>]>[+[-<+>]>+>>]<<<<<]` twice to extract hundreds, tens, and units digits, with leading zero suppression.

## Limitations
- 8-bit arithmetic: numbers and results must fit in 0-255
- All 6 benchmark test cases and 17 additional edge cases pass

## Code Length
5023 characters
