# H10: Remove Consecutive Duplicates

## Approach
Read characters one at a time. For each character, compare it with the
previous character. If they differ (or there is no previous character),
output the current character. Then update "previous" to the current
character and continue.

## Tape Layout
- Cell 0: previous character (initially 0)
- Cell 1: current character (input read here)
- Cell 2: difference (current - previous), used for comparison
- Cell 3: copy of previous (consumed during subtraction)
- Cell 4: temporary cell for non-destructive copies

## Algorithm Detail
1. Read a character into cell 1.
2. Loop while cell 1 is nonzero (i.e., not EOF):
   a. Non-destructively copy current (cell 1) to cell 2.
   b. Non-destructively copy previous (cell 0) to cell 3.
   c. Subtract cell 3 from cell 2 (both destroyed), leaving
      diff = current - previous in cell 2.
   d. If cell 2 is nonzero, output cell 1 (current character).
   e. Update previous: clear cell 0 and copy cell 1 into it.
   f. Read next character into cell 1.
3. End loop.

The first character is always output because previous starts at 0
(which differs from any printable ASCII character).

## Evidence (Test Results)
All 6 provided test cases pass:
- 'aaabbbbcc' -> 'abc'
- 'hellooo' -> 'helo'
- 'xyz' -> 'xyz'
- 'aabbccdd' -> 'abcd'
- 'a' -> 'a'
- 'mississippi' -> 'misisipi'

## Difficulty Assessment
Easy-to-medium. The core logic (compare current with previous, output
if different) is straightforward. The main challenge in Brainfuck is
implementing non-destructive comparison, which requires temporary cells
and careful cell management.

## Design Choices
- Used subtraction-based comparison: compute (current - previous) and
  check if nonzero. This works because equal characters yield zero and
  unequal ones yield nonzero (wrapping arithmetic is fine for this
  check since we only care about zero vs. nonzero).
- Previous starts at 0, ensuring the first character is always output
  (since no printable ASCII character has value 0).
- Used the framework's `copy` helper for non-destructive copies and
  manual subtract loop for the comparison.

## Assumptions
- EOF is represented as 0 (standard for Brainfuck).
- Input consists of printable ASCII characters (none with value 0).
- Wrapping 8-bit cells (standard), though the algorithm works with any
  cell size since we only test for zero vs. nonzero difference.

## Critique
- The code could be slightly shorter by inlining some operations or
  reusing cells more aggressively, but clarity and correctness were
  prioritized over code golf.
- The clear operations before copy are sometimes redundant (the cells
  are already zero), but they serve as safety nets and cost very little.
