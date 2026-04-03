# M15 Anagram Test - Brainfuck Solution

## Algorithm
Frequency counting approach:
- For each character in string 1: increment freq[char - 97]
- For each character in string 2: decrement freq[char - 97]
- If all 26 frequency counters are zero: anagrams ("yes"), otherwise "no"

## Tape Layout
- Cell 0: input character / workspace
- Cell 1: temp
- Cell 2: sentinel (always 0, used as shuttle return marker)
- Cells 3,5,7,...,53: freq[0..25] for letters a-z
- Cells 4,6,8,...,54: shuttle workspace

## Key Technique
Uses a shuttle pattern to dynamically navigate to freq[char-97]:
- Forward: decrement-and-shift with breadcrumb trail
- Backward: follow breadcrumbs clearing them

## Code Size
1369 characters

## Test Results
All 6 tests passed.
