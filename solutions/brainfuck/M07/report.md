# M07 Factorial - Brainfuck Solution

## Approach
Lookup table: parse input N (0-10), then switch on N to print the precomputed factorial string.

## Input Parsing
- Read first character, convert from ASCII digit
- Read second character: if it's '0' (for input "10"), multiply first digit by 10
- This handles both single-digit (0-9) and two-digit (10) inputs

## Switch Structure
- Uses a "not_done" flag and checks N == 0, 1, 2, ..., 10 sequentially
- For each case, copies N and tests if zero; if matched, prints the factorial string
- After printing, clears the not_done flag to skip remaining cases
- If not matched, decrements N and proceeds to next case

## Code size
3461 characters

## Test results
All 11 test cases passed (N = 0 through 10).
