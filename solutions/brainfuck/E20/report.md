# E20: Compare Two Integers - Brainfuck Solution

## Approach
Parse two possibly-negative integers from ASCII input, compare them, and output "less", "greater", or "equal".

## Algorithm
1. **Input parsing**: Read each integer character by character, detecting minus sign (ASCII 45) and accumulating digits via multiply-by-10-and-add. For integer A, digits end at space (ASCII 32). For integer B, digits end at EOF (0), newline (10), or CR (13).

2. **Normalization**: Clear the sign flag if magnitude is 0 (handles -0 = 0 case).

3. **Sign-based comparison**:
   - If signs differ, the negative number is less.
   - If signs are the same, compare magnitudes by simultaneous decrement.

4. **Magnitude comparison** (same sign):
   - Decrement both values simultaneously until one reaches zero.
   - If both reach zero: "equal"
   - If A reaches zero first: A has smaller magnitude
   - If B reaches zero first: B has smaller magnitude
   - XOR the magnitude comparison result with the sign to determine final output.
   - For positive numbers, smaller magnitude = "less"
   - For negative numbers, smaller magnitude = "greater"

5. **Output**: Print the result string using character-by-character ASCII output with delta encoding.

## Evidence
All 6 official test cases pass, plus 15 additional edge cases including negative numbers, zero comparisons, -0 handling, and three-digit values.

## Difficulties
- Decimal number parsing in BF requires careful management of multiply-by-10 accumulation.
- Sign handling adds complexity with XOR logic for the negative-magnitude-reversal case.
- "Is digit" detection for the second number requires checking against multiple terminator values (0, 10, 13).
- BF's lack of if-else requires flag-based conditional execution patterns.
- "Already printed" state must be tracked in a dedicated cell (DONE) separate from control-flow flags to avoid being consumed by BF's loop-based conditionals.

## Difficulty Assessment
High. This problem combines several non-trivial BF sub-problems: decimal parsing with sign handling, multi-way branching (3 possible outputs), and magnitude comparison with sign-dependent reversal.

## Design Choices
- Used 12 tape cells with named positions for clarity.
- Dedicated DONE cell to track whether output has already been produced, avoiding re-execution of output branches.
- Simultaneous decrement for magnitude comparison (O(n) where n = max magnitude).
- XOR of sign and magnitude-comparison-result to determine "less" vs "greater" in same-sign case.
- Handles -0 by clearing sign when magnitude is 0.

## Assumptions
- Input is well-formed: two integers separated by a single space.
- Integer magnitudes fit in a single 8-bit cell (0-255).
- Input terminates with EOF, newline, or CR after the second integer.

## Critique
- The code is long (~4KB) due to BF's verbosity, but each section is logically clean.
- The simultaneous-decrement approach is O(max_magnitude) which is fine for values up to 255.
- Could be optimized by using subtraction instead of simultaneous decrement, but correctness is prioritized.
- The -0 normalization is a defensive measure that costs minimal code.
