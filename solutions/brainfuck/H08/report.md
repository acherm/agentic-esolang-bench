# H08: Digit Frequency - Brainfuck Solution

## Problem
Read a string of digits 0-9. Count the frequency of each digit and output ten space-separated integers representing counts for digits 0 through 9.

## Approach
The solution uses two phases:

### Phase 1: Input and Counting
- Cells 0-9 serve as counters for each digit (0-9 respectively)
- Read each input character into cell 10
- Subtract 48 (ASCII '0') to get the digit value d (0-9)
- For each digit k in 0-9, perform a non-destructive equality check: copy d to a temp cell, subtract k, and test for zero
- If d == k, increment cell[k]
- The equality check uses the standard BF pattern: set flag=1, if value nonzero then clear flag, then if flag is set the values were equal

### Phase 2: Decimal Output
- For each counter cell k (0-9), copy the count to a workspace area
- Convert count to decimal using repeated-subtraction divmod:
  - Divide by 100 to get hundreds digit, remainder becomes new value
  - Divide by 10 to get tens digit, remainder is ones digit
- The divmod uses a countdown timer: set countdown=divisor, decrement alongside value, when countdown hits zero increment quotient and reset. After the loop, remainder = divisor - countdown.
- Output with leading zero suppression: skip leading zeros but always print at least the ones digit
- Print space between consecutive numbers

## Tape Layout
- Cells 0-9: digit frequency counters
- Cell 10: input character / digit value
- Cells 11-14: scratch for digit matching (copy temp, comparison, flag)
- Cells 20-31: decimal output workspace (value, quotient, countdown, flags, digit storage, char output)

## Evidence of Correctness
All 6 benchmark test cases pass. Additionally tested with:
- Large single-digit counts (20, 50, 100, 200) - multi-digit decimal output works correctly
- Single character input
- Mixed distributions

## Difficulties
- BF lacks indirect addressing, so incrementing cell[d] for variable d required 10 explicit equality checks per input character
- Divmod in BF requires careful cell management: the countdown-to-zero detection needs a non-destructive copy of the countdown value (copy to two temps, restore from one, test with the other)
- Leading zero suppression for decimal output adds complexity (check hundreds > 0, then tens > 0 OR hundreds was printed)

## Difficulty Assessment
Hard. The combination of (1) variable-indexed cell increment, (2) divmod for decimal output, and (3) leading zero suppression makes this substantially more complex than simple BF programs. The code is ~14K characters.

## Design Choices
- Used 10 explicit equality checks rather than trying to simulate indirect addressing, trading code size for simplicity and correctness
- Allocated generous tape space (32 cells) to avoid cell conflicts between the counting and output phases
- Divmod uses countdown timer approach rather than repeated full subtraction, which is cleaner in BF
- Output workspace is separate from counter cells to avoid corruption during output

## Assumptions
- Input consists only of ASCII digits 0-9 (as specified)
- EOF returns 0 (confirmed from interpreter source)
- 8-bit wrapping cells (mod 256) - counts above 255 would wrap, but this is a BF limitation
- No newline at end of output (matches expected test output)

## Critique
- Code is ~14K chars, which is large but unavoidable given BF constraints
- The 10-check-per-character approach is O(10n) for n input characters, but each check is constant-time BF operations
- Could potentially use a shuttle/walk technique to reduce code size, but the explicit check approach is more reliable and easier to verify
- The divmod could be factored into a reusable subroutine in the generator, which was done via the divmod_cells function
