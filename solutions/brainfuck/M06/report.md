# M06: Greatest Common Divisor - Brainfuck Solution

## Algorithm
Euclidean algorithm: while B != 0, compute (A, B) = (B, A mod B).

A mod B is computed via count-down: decrement a counter initialized to B
for each unit of A. When the counter hits zero, reload from B and count
a quotient. The remainder is B minus the final counter value.

## Input parsing
- First number: read chars until space (subtract 32, loop while nonzero).
- Second number: read chars until EOF/newline (check for zero and newline).
  Each digit accumulated via multiply-by-10-and-add.

## Output
Extract digits via divmod by 100 then by 10 (up to 3 digits for values 0-255).
Leading-zero suppression ensures correct formatting.

## Code size
1870 characters of Brainfuck.
