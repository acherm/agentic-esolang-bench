# H05 - Big Integer Addition (Brainfuck)

## Algorithm
1. Read first number with insert-at-front reversal into A-track (LSB first, digit+1 encoding)
2. Read second number with insert-at-front reversal into B-track (interleaved with A)
3. Add digit by digit with carry propagation
4. Output result MSB-first by traversing A-track right to left

## Tape Layout (stride 6)
- Cells 0-11: I/O scratch and sentinels
- Cell 12+6k: A-track (sentinel at 12, digits at 18, 24, 30, ...)
- Cell 13+6k: B-track
- Cell 14+6k: C-track (carry)
- Cell 15+6k: T (temp)
- Cell 16+6k: F (flag)
- Cell 17+6k: G (temp)

## Key Techniques
- Insert-at-front with stride-6 shift for natural reversal during input
- Paired decrement for carry detection (sum >= 10 check)
- digit+1 encoding (1-10 for digits 0-9, 0 as sentinel)

## Code size
794 characters
