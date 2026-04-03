# M02 Word Count - Brainfuck Solution

## Algorithm
1. Initialize count = 1 (at least one word)
2. Read each character; if space (ASCII 32), increment count
3. After all input, output count as decimal number

## Decimal Output
Uses two divmod-by-10 operations to extract hundreds, tens, ones digits.
Leading zeros are suppressed.

## Code Length
1244 characters
