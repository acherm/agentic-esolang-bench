# H18: Divisible By 3

## Approach
Ring counter mod-3 technique. Three cells (R0, R1, R2) form a ring where exactly
one cell holds value 1 at any time, indicating the current sum-of-digits mod 3.

For each input digit:
1. Read ASCII character, subtract 48 to get numeric value d (0-9)
2. Rotate the ring counter d times (R0->TEMP, R1->R0, R2->R1, TEMP->R2)

After all input, R0 being nonzero means sum mod 3 == 0 (divisible by 3).

## Evidence
All 6 test cases pass, including edge cases: single digits (0, 1, 9),
multi-digit (11, 123456), and large input (999999999).

## Difficulties
The main challenge was implementing mod-3 in Brainfuck. Direct subtraction-based
approaches require "if equals" logic which is awkward in BF. The ring counter
approach avoids conditional comparisons entirely by using structural rotation.

## Difficulty Assessment
Medium. The digit-sum divisibility rule simplifies the math, but implementing
modular arithmetic in BF requires a non-obvious technique (ring counter).

## Design Choices
- **Ring counter over subtraction**: Avoids the need for comparison/branching
  to detect when a value equals 3, which is notoriously difficult in BF.
- **Rolling mod**: Each digit is processed immediately rather than accumulating
  a large sum, preventing overflow for long inputs.
- **EOF = 0**: The interpreter returns 0 on EOF, which naturally terminates
  the input loop since 0 is the loop-exit condition.

## Assumptions
- EOF returns 0 (verified with the interpreter)
- Input contains only ASCII digit characters (0-9) with no trailing newline
- 8-bit wrapping cells (standard BF)

## Critique
The rotation loop executes d times per digit (up to 9 rotations per digit),
with each rotation involving 4 move operations. For very long inputs this is
O(n * avg_digit_value) but remains efficient since digit values are bounded
by 9. The code is concise and correct. An alternative approach using lookup
tables could be faster per digit but would require significantly more code.
