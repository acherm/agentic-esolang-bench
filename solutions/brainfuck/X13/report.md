# X13: Valid Parentheses Types - Brainfuck Solution

## Algorithm
Stack-based bracket matching using BF data pointer as stack pointer.

- Cell 0 is a sentinel (always 0) marking empty stack
- Stack grows rightward: cells 1, 2, 3, ...
- For each opener (parens/brackets/braces), push the expected closer onto the stack
- For each closer, compare with stack top:
  - Match: pop (clear cells, move pointer left)
  - Mismatch or empty stack: push error marker (1)
- At EOF: if stack is empty (at sentinel) output "yes", else "no"

## Character classification
Serial subtraction on a copy of the input char to check against ASCII 40, 91, 123 (openers).
Mathematical proof that no false positives occur among the 6 bracket characters.

## Pointer movement trick
Conditional pointer adjustment using cell[2] as pop indicator:
`[-<<]<` moves ptr by -1 (push/stay) or -3 (pop) from cell[2], unifying both cases.

## Code length: 1524 characters
