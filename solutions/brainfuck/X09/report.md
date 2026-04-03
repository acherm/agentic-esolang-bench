# X09 - Bracket Depth Maximum (Brainfuck)

## Algorithm
- Read input character by character until EOF (cell reads 0)
- For each '(' (ASCII 40): increment depth counter; if depth > max then max = depth
- For each ')' (ASCII 41): if depth > 0, decrement depth (clamped at 0 for unmatched close parens)
- After all input, output max depth as a decimal number

## Key Insight for Max Update
Since depth only increases by 1 at a time, depth > max implies depth == max + 1.
Before incrementing depth for '(', we check if depth == max (by computing max - depth).
If equal, after incrementing depth we also increment max.

## Tape Layout
- Cell 0: input character
- Cell 1: depth counter
- Cell 2: max depth
- Cells 3-5: temporaries for comparison and branching
- Cells 6-12: workspace for decimal output (two passes of divmod by 10)

## Decimal Output
Uses the standard BF divmod algorithm `[->-[>+>>]>[+[-<+>]>+>>]<<<<<]` twice
to extract hundreds, tens, and ones digits, then prints with leading zero suppression.

## Code Length
887 characters

## Test Results
All 6 specification tests passed.
All 6 additional edge case tests passed (including empty input, double-digit output).
