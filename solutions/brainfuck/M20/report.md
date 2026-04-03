# M20 - Count Distinct Characters (Brainfuck)

## Algorithm
Uses a 3-cells-per-entry flag array (nav/ret/flag) starting at cell 6.
For each input character with ASCII value V, navigates to entry V using a
forward shuttle technique, checks the flag, sets it if new (incrementing count),
then navigates back using a reverse shuttle with the return counter.

After all input, performs two divmod-by-10 operations to extract hundreds, tens,
and ones digits, then prints with leading-zero suppression.

## Tape Layout
- Cell 0: input char / quotient workspace
- Cell 1: count / divmod counter
- Cells 2-5: temporaries for divmod and output
- Cells 6+: 3-cell entries [nav, ret, flag] for ASCII lookup

## Code size
605 characters
