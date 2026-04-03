# H16 - Longest Run Length (Brainfuck)

## Approach
Track previous character, current run length, and maximum run length.
For each input character, compare with previous:
- Same: increment current run
- Different: compare current run with max (update if larger), reset to 1
After all input, do final comparison, then output max as decimal.

## Key Design Choices
- **Saturating decrement** for safe conditional subtraction (avoids 8-bit wrapping issues)
- **Comparison via simultaneous countdown**: copy CUR and MAX, decrement MAX copy from CUR copy using sat_dec; remainder = max(0, CUR-MAX); add to MAX
- **Decimal output** via repeated trial subtraction (divmod by 100 then 10), with leading zero suppression
- **If-else pattern**: use a flag cell set to 1, cleared in the if-branch, checked in else-branch

## Evidence
All test cases pass.

## Difficulties
- Implementing comparison (greater-than) in Brainfuck required a saturating decrement primitive
- Decimal output required careful divmod implementation with conditional decrement and rollback on failure
- If-else branching in BF requires careful flag management

## Difficulty Assessment
Hard. The core run-length logic is straightforward, but BF comparison and decimal output are non-trivial.

## Assumptions
- 8-bit wrapping cells (standard BF)
- EOF returns 0
- Input is non-empty (at least 1 character)
- Run lengths fit in 8-bit cell (max 255)

## Critique
- Code is long (~several KB) due to BF's verbosity for arithmetic
- The divmod loop for decimal output is the most complex part
- Could be shortened with more aggressive code optimization
- The saturating decrement approach is correct but generates O(n) BF operations per comparison step
