# X05: Merge Two Sorted Arrays (Brainfuck)

## Approach
1. **Input Parsing**: Read decimal integers (including negative) character-by-character from ASCII input, using offset encoding (value + 128) to handle negative numbers in single BF cells.
2. **Bubble Sort**: Since both input arrays are already sorted, a simple bubble sort efficiently merges them after concatenation. The sort uses simultaneous decrement comparison of offset-encoded values.
3. **Output**: Decode offset-encoded values back to signed integers, convert to decimal ASCII, and print with space separators.

## Implementation Details
- **Offset encoding**: Each integer is stored as (value + 128), mapping [-127, 127] to [1, 255]. Cell value 0 serves as a sentinel/empty marker.
- **Unrolled parsing**: Up to 20 numbers are parsed using unrolled inline code at known tape positions, with a fixed workspace area for each parse operation.
- **Character classification**: Input characters are classified via cascading subtraction (EOF=0, newline=10, space=32, minus=45, digits=48-57).
- **Division by 10**: Used for decimal output via repeated subtraction with a modular counter.

## Tape Layout
- Cells 0: left boundary (always 0)
- Cells 1-20: array values (offset-encoded, 0 = sentinel)
- Cells 200-220: parsing workspace
- Cells 230-240: comparison/sort workspace
- Cells 260-280: output workspace
