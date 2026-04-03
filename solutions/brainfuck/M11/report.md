# M11 - Substring Occurrences (Brainfuck)

## Problem
Read string S and pattern P. Count overlapping occurrences of P in S.

## Approach
Uses a stride-6 interleaved tape layout where text[k] and pattern[k] are stored 1 cell apart, enabling trivial in-place comparison.

### Tape Layout (stride 6, data at cell 7+)
- Cell 0: counter
- Cells 1-6: temps/sentinels
- Cell[7+6k+0]: text[k]
- Cell[7+6k+1]: pattern[k]
- Cell[7+6k+2]: diff (comparison result)
- Cell[7+6k+3-4]: scratch
- Cell[7+6k+5]: marker (navigation)

### Algorithm
1. Read text into stride-6 text cells until newline
2. Navigate back, read pattern into interleaved pattern cells until EOF
3. For each text position (outer loop):
   - Compare text[0..P-1] with pattern[0..P-1] in inner loop
   - Collect boolean mismatch flags backward into accumulator cell
   - If accumulator = 0 (all matched), increment counter
   - Shift text left by one stride position
4. Output counter as decimal

### Key Techniques
- **Interleaved storage**: text[k] and pattern[k] are adjacent, so comparison uses only local cell operations
- **Marker scanning**: nonzero marker cells enable [<<<<<<] navigation back to start
- **Backward diff collection**: mismatch booleans are cascaded left to a known accumulator cell
- **Non-destructive comparison**: text and pattern values are preserved via copy-restore using scratch cells

## Code size
778 characters

## Test results
All 6 benchmark tests pass. Additional edge cases verified (14 total tests).
