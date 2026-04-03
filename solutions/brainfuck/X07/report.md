# X07: Longest Palindromic Substring Length (Brainfuck)

## Algorithm
Brute-force check of all possible substrings from longest to shortest.
For each length L from 7 down to 1, and each starting position, check:
1. All characters in the range exist (are nonzero / within string bounds)
2. The substring is a palindrome (compare character pairs from outside in)

The first palindrome found is the longest. Output its length as an ASCII digit.

## Implementation Details
- String stored in cells 10-16 (max 7 characters)
- Cells 0-9 used as workspace for comparisons
- Non-destructive cell comparison using copy-compare technique
- Early exit: once a palindrome is found, all subsequent checks are skipped
- O(n^2) substring checks, O(n) comparison per check = O(n^3) total
- For n <= 7, this is very fast

## Memory Layout
- Cells 0-3: temporary cells for comparison operations
- Cell 4: comparison result (1 if equal, 0 if not)
- Cell 5: AND accumulator for palindrome check
- Cell 6: found flag (1 once answer is output)
- Cell 7: temp for found check
- Cell 8: current length cell
- Cell 9: temp
- Cells 10-16: string characters
- Cell 17: null terminator
