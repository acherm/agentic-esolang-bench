# H06: Longest Word (Brainfuck)

## Problem
Read a line of space-separated words. Output the longest word (first if tied).

## Algorithm
Two-pass approach using 8-cell interleaved groups with the "carry" technique.

### Tape Layout
- Cells 0-7: padding (always 0, navigation boundary)
- Groups of 8 cells: [B][W][F][C][t1][t2][t3][t4]
  - B: carries best/max word length
  - W: carries current word length
  - F: flag (1=input present, 0=EOF/padding)
  - C: character (char-32; space=0, letters=1-94)
  - t1-t4: comparison temporaries

### Pass 1: Find max word length
- Carry B (max) and W (current length) forward through letters
- At word boundaries: compare W > B, update B = max(B, W)

### Pass 2: Find and output first matching word
- Navigate back carrying B (max length)
- Re-scan with carry, check W == B at boundaries
- On match: navigate back by W groups, output chars (+32)

## Code size: 1955 characters
