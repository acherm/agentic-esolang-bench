# M12 - Remove Vowels (Brainfuck)

## Approach
For each input character, check if it matches any of the 10 vowel characters
(a, e, i, o, u, A, E, I, O, U). If it does not match any vowel, output it.

### Tape Layout
- Cell 0: Input character (preserved across checks)
- Cell 1: Work cell (copy of char for subtraction)
- Cell 2: Output flag (1 = not a vowel, 0 = is a vowel)
- Cell 3: Temp cell (used for non-destructive copy and zero-check)

### Per-Character Algorithm
1. Read a character into cell 0
2. Set flag (cell 2) = 1
3. For each of the 10 vowels:
   a. Copy cell 0 to cell 1 (non-destructive, using cell 3 as temp)
   b. Subtract the vowel's ASCII value from cell 1
   c. If cell 1 == 0 (character matches this vowel), clear the flag
4. If the flag is still 1, output the character
5. Read next character; loop until EOF (cell 0 = 0)

### Zero-Check Pattern
To test if a cell equals zero without a direct "if-zero" instruction:
- Set temp = 1
- If work cell is nonzero: decrement temp, clear work cell
- If temp is still 1: the work cell was zero (match found), so clear the flag

## Evidence
All test cases pass:
- 'hello' -> 'hll' (removes e, o)
- 'Esoteric' -> 'strc' (removes E, o, e, i)
- 'xyz' -> 'xyz' (no vowels, unchanged)
- 'AEIOU' -> '' (all uppercase vowels removed)
- 'brainfuck' -> 'brnfck' (removes a, i, u)
- 'test' -> 'tst' (removes e)

## Difficulties
- BF has no equality comparison, so checking "if cell == value" requires:
  subtracting the value and then testing for zero, which itself requires
  a temp cell and careful logic.
- Non-destructive copy of the input character is needed for each of 10 vowel
  checks, requiring a restore-from-temp pattern.
- The code is lengthy due to 10 repeated vowel checks, each involving
  a full copy + subtract + zero-check sequence.

## Difficulty Assessment
Medium. The core challenge is implementing equality checks for 10 different
values. Each check follows the same pattern but with different subtraction
constants. The pattern itself (copy, subtract, zero-check with flag) is a
well-known BF idiom.

## Design Choices
- Used a flag-based approach (start with flag=1, clear on match) rather than
  trying to build a single conditional. This is simpler and more reliable.
- Checked all 10 vowels sequentially. An alternative would be range-based
  checks, but that would be more complex and error-prone.
- Used 4 tape cells total, keeping memory usage minimal.

## Assumptions
- EOF returns 0 (confirmed by interpreter source code).
- Input contains only printable ASCII characters (no null bytes in the middle).
- Input has no trailing newline (confirmed by examining test data).

## Critique
- The code is long due to the repeated pattern for each vowel. A more compact
  approach might use a lookup table or arithmetic tricks, but the straightforward
  approach is more reliable and easier to verify.
- The algorithm is O(n * 10) where n is input length, with each vowel check
  doing O(V) BF operations where V is the vowel's ASCII value (for the copy
  and subtract steps). This is efficient enough for the problem constraints.
