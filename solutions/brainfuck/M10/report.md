# M10 — Binary To Decimal (Brainfuck)

## Algorithm
1. Read binary digits left-to-right, building accumulator: acc = acc*2 + bit
2. Convert accumulator (0-255) to decimal string using two divmod-by-10 operations
3. Print digits with leading-zero suppression (hundreds, tens, ones)

## Tape Layout
- Cell 0: accumulator / print flag
- Cell 1: ones digit (after divmod) / temp
- Cell 2: quotient / tens counter / temp
- Cell 3: hundreds digit / input char / countdown
- Cell 4: tens digit / temp flag
- Cells 5-9: temporaries for divmod and printing

## Code Size
960 characters
