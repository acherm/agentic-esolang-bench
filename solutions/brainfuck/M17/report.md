# M17: Replace Spaces With Underscores (Brainfuck)

## Approach
Character-by-character processing with equality check against ASCII 32 (space).

**Tape layout:** 5 cells
- Cell 0: input character
- Cell 1: comparison copy (subtract 32 to check for space)
- Cell 2: output character (input copy, overwritten to 95 if space)
- Cell 3: flag (1 = was a space)
- Cell 4: temp for non-destructive copy

**Algorithm per character:**
1. Read character; if EOF (0), stop
2. Copy to cells 1 (comparison) and 2 (output candidate)
3. Subtract 32 from cell 1
4. Set flag = 1
5. If cell 1 nonzero (not space): clear flag
6. If flag set (was space): set cell 2 = 95 ('_')
7. Output cell 2

## Evidence
All 6 problem test cases pass. All 6 additional edge cases pass (empty input, single space, single char, spaces at edges, no spaces, mixed).

## Difficulties
Low. The main challenge is implementing equality comparison in BF (which lacks direct comparison operators). The standard flag-based pattern handles this cleanly.

## Difficulty Assessment
Easy-to-medium. Single-character transformation with one comparison value.

## Design Choices
- Used 5-cell layout for clarity and correctness
- Non-destructive copy pattern (copy + restore via temp) preserves input for the loop condition
- Flag-based zero-check pattern is the standard BF idiom for equality testing

## Assumptions
- EOF returns 0 (confirmed by testing the interpreter)
- Input is a single line of printable ASCII text
- No newline in output (problem examples show none)

## Critique
- The code could be slightly shorter by using a more compact cell layout, but clarity was prioritized
- The 95 '+' characters for underscore ASCII value are verbose but unavoidable in BF
- Could optimize by computing 95 via multiplication loop, but this adds complexity with no functional benefit
