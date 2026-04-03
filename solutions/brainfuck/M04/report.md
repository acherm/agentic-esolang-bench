# M04 – Caesar Shift By 3

## Problem
Read a lowercase alphabetic string, shift each letter forward by 3 positions
in the English alphabet (wrapping z→c), and output the transformed string.

## Approach
For each character:
1. Read the character
2. Check if it's one of x, y, z (which need wrap-around)
3. Add 3 to the character
4. If wrap needed (was x/y/z), subtract 26
5. Output the result

The wrap detection works by subtracting 120 ('x') from a copy of the input character.
If the result is 0, 1, or 2, the character was x, y, or z respectively.
Three sequential "is zero" checks using the standard BF flag pattern detect each case.

## Cell Layout
- c0: input char / output char
- c1: test value (char - 120), then decremented for each check
- c2: temp for copy operations
- c3: flag for "is zero" check
- c4: wrap flag (1 if char is x, y, or z)
- c5: backup of test value between checks

## Code Size
394 characters of Brainfuck.
