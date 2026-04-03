# M19 - Characters At Even Indices (Brainfuck)

## Approach
Read characters and output those at even (0-based) indices. The algorithm alternates
between outputting (even index) and discarding (odd index) characters.

## Design
- **Tape layout**: Cell 0 holds the current character, Cell 1 is a temporary flag.
- **Main loop**: Read even-index char, output it, read odd-index char.
  - If odd-index read returns EOF (0), the main loop exits naturally.
  - If odd-index read returns a character, use a flag-based "if nonzero" pattern
    to read the next even-index char, then loop back.
- The "if nonzero" pattern works by: entering a loop on cell 0 (only if nonzero),
  clearing cell 0, setting a flag in cell 1, then exiting. A second block checks
  the flag and performs the read.

## Assumptions
- EOF is represented as 0 (standard BF convention).
- Input contains no null (0) bytes.

## Difficulty Assessment
Medium-easy. The main challenge is implementing conditional logic ("if nonzero, read
another char") in BF, which lacks native if-else. The flag-cell pattern solves this
cleanly.

## Critique
The solution uses 2 cells and a straightforward flag pattern. It could be slightly
shorter with hand-written BF, but the generated code is clear and correct. The approach
handles all edge cases: single char, empty input (EOF immediately), even-length strings,
and odd-length strings.
