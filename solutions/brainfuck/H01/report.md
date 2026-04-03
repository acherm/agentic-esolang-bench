# H01 - Balanced Parentheses (Brainfuck)

## Algorithm
- Maintain a depth counter and error flag
- For each '(': increment depth
- For each ')': if depth == 0, set error flag; else decrement depth
- After input: if depth == 0 AND no error -> "yes", else "no"

## Tape Layout
- Cell 0: input character / scratch
- Cell 1: depth counter
- Cell 2: error flag
- Cells 3-6: temporaries
- Cell 7: output character

## Code Length
860 characters
