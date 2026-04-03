# E06: Even Or Odd

## Approach
1. Read all characters until EOF, keeping only the last character (which is the last digit).
2. Subtract 48 (ASCII '0') to get the numeric digit value (0-9).
3. Compute value mod 2 using a toggle: decrement value one at a time, flipping a result cell between 0 and 1 each time.
4. If result is 0 (even), print "even". If result is 1 (odd), print "odd".

## Key insight
A number's parity depends only on its last digit. Negative signs don't affect parity.

## Code length
443 characters
