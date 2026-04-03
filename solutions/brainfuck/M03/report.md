# M03 - Run Length Encoding (Brainfuck)

## Problem
Read a string and produce its run-length encoding: for each maximal block of
identical characters, output the character followed by the block length as a
decimal integer.

## Algorithm
1. Read the first character as the current run character, set count = 1.
2. Read the next character:
   - If same as current: increment count.
   - If different or EOF: output current char + count as decimal digits,
     then set the new character as current and reset count to 1.
3. Repeat until EOF.

## Tape Layout
- Cell 0: Current character (run character)
- Cell 1: Next input character
- Cell 2: Run count
- Cells 3-7: Temporaries for comparison/flags
- Cells 8-10: Digit cells (hundreds, tens, ones)
- Cells 11-17: Division workspace and flags

## Multi-digit Output
Count is converted to decimal using repeated divmod-by-10 via subtraction loops.
Leading zeros are suppressed. Supports counts up to 255 (3 digits max).

## Code size
1131 characters
