# H20 - Sort Strings Lexicographically (Brainfuck)

## Approach
- Fixed-slot bubble sort with SLOT_SIZE=8, MAX_N=5
- Parse single-digit N, read N strings into fixed-size memory slots
- Fill unused slots with 0xFF so they sort after valid strings
- Bubble sort using unrolled passes comparing adjacent slot pairs char-by-char
- Lexicographic comparison via simultaneous decrement of char values
- Output sorted strings separated by spaces

## Implementation
- Generated procedurally using a Python BF code generator
- Memory layout: 20 header cells for counters/temps, then 5 slots of 8 cells each
- Uses "execute once if" pattern to avoid infinite loops in BF conditionals
- Comparison: simultaneous decrement of copied char values to determine ordering
- Swap: cell-by-cell exchange of entire slots using a temp cell

## Result
All test cases pass.
