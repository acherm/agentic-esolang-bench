# E12 - Minimum Of Two (Brainfuck)

## Approach
The solution parses two signed decimal integers separated by whitespace, compares them
considering signs, and outputs the minimum as a decimal string.

### Parsing
- Reads first character, checks for '-' (ASCII 45) to detect negative sign
- Accumulates digits: val = val * 10 + (char - 48)
- Stops at space (ASCII 32) for first number
- For second number, stops at EOF (0), newline (10), or CR (13)

### Comparison
Four cases handled:
1. A positive, B negative -> B is smaller
2. A negative, B positive -> A is smaller
3. Both positive -> smaller magnitude is smaller
4. Both negative -> larger magnitude is smaller (more negative)

For same-sign comparison: copies both magnitudes and decrements simultaneously until
one reaches zero, then determines which is smaller based on sign.

### Output
- Prints '-' if result is negative
- Divides magnitude by 10 twice to get hundreds, tens, ones digits
- Uses countdown-based divmod (count down from 10, reset on zero)
- Suppresses leading zeros

## Evidence
All 6 test cases pass including negative numbers, zero, and three-digit numbers.

## Difficulties
- Implementing if-else logic in BF requires flag-based patterns
- Divmod in BF with 8-bit wrapping cells requires careful countdown approach
- Same-sign comparison needs sign-dependent interpretation of magnitude comparison
- Leading zero suppression in output requires nested conditionals

## Difficulty Assessment
Medium-hard for BF. The core algorithm (compare two numbers) is simple, but the BF
implementation is complex due to: signed number parsing, four-case sign comparison,
and decimal output with divmod.

## Design Choices
- Tape layout uses 28 cells with named positions for clarity
- Countdown-based divmod avoids underflow detection issues
- Flag-based if-else pattern used throughout for conditional logic
- Simultaneous decrement for magnitude comparison

## Assumptions
- Input is two integers separated by a single space
- Numbers fit in a byte (0-255 magnitude), covering the test range of -100 to 100
- EOF returns 0 (standard BF behavior)
- 8-bit wrapping cells (verified)

## Critique
- The code is long (~3500+ chars) due to BF's verbosity for arithmetic
- Could be shorter with more aggressive cell reuse
- The parsing could be more robust for multiple spaces or tabs
- Limited to numbers with magnitude <= 255 due to 8-bit cells
