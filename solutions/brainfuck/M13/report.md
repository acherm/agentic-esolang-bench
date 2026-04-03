# M13 Sort Numbers - Brainfuck Solution

## Algorithm
- Parse N integers with carry-N approach (stride-8 records, offset+128 encoding)
- Bubble sort with N-1 passes (count stored during parsing)
- Output sorted values as signed decimal with space separation

## Key Techniques
- Carry-N parsing: N counter travels with data pointer
- Offset+128 encoding for signed values in unsigned 8-bit cells
- Cell 0 = 255 marker for left-boundary detection in navigation
- Count-based sort termination (N-1 passes, no swap detection needed)
- Simultaneous countdown for value comparison (sort and sign detection)
- Divmod by 100/10 for decimal digit extraction with leading zero suppression
