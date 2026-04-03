# E03 Hello Name - Brainfuck Solution

## Approach

The solution uses a two-cell tape layout:
- **Cell 0** serves as a scratch cell for printing constant characters ("Hello, " prefix and "!" suffix).
- **Cell 1** is used for reading input characters and echoing them back.

The algorithm proceeds in three phases:
1. Print the fixed prefix "Hello, " using `print_string`, which sets cell 0 to each character's ASCII value (using incremental +/- adjustments) and outputs it.
2. Enter an input echo loop: read a character into cell 1, and while it is nonzero (i.e., not EOF), print it and read the next character.
3. After the loop terminates (EOF returns 0 in this interpreter), print "!" by setting cell 0 to ord('!') = 33 and outputting it.

## Evidence

All 6 specification tests pass:
- "Aman"   -> "Hello, Aman!"
- "Ada"    -> "Hello, Ada!"
- "Lambda" -> "Hello, Lambda!"
- "X"      -> "Hello, X!"
- "World"  -> "Hello, World!"
- "123"    -> "Hello, 123!"

## Difficulties

- **EOF behavior**: The main concern was how the interpreter handles EOF on `,` (read). Testing confirmed it returns 0, which is the most common BF convention and allows a simple `[.,]`-style echo loop.
- **No trailing newline**: The input is provided without a trailing newline, so there is no need to strip or skip a newline character before printing "!".

## Difficulty Assessment

**Easy**. This is a straightforward string concatenation problem. The BF implementation only requires printing a constant prefix, echoing input, and printing a constant suffix. The two-cell layout keeps the solution minimal.

## Design Choices

- **Incremental character output**: `print_string` computes the difference between consecutive characters to minimize the number of `+`/`-` operations, rather than clearing and rebuilding each character from zero.
- **Separate cells for constants vs. input**: Keeping the constant-printing cell (0) separate from the input cell (1) avoids interference and makes the logic cleaner. After the echo loop, cell 0 still holds the last printed constant character's value, but `print_char` clears it before setting the new value, so no stale state issues arise.

## Assumptions

- EOF on `,` returns 0 (confirmed by testing the interpreter).
- Input does not contain a trailing newline (confirmed by testing).
- Input contains only printable ASCII characters (as implied by the test cases).

## Critique of the Problem

The problem is well-defined and appropriate for an "easy" difficulty tier. The specification is clear: read a name, wrap it in "Hello, " and "!". The test cases cover single-character names, multi-character names, and numeric strings, providing reasonable coverage. One minor observation is that the problem does not test edge cases like empty input (no name), which would produce "Hello, !" -- but this is acceptable for the stated difficulty level.
