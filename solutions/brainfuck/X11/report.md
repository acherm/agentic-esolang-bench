# X11 - Count Inversions (Brainfuck)

## Approach
O(n^2) brute-force with unrolled pair comparisons: for each pair (i,j) with
i < j, compare a[i] > a[j] using simultaneous decrement, and increment a
counter for each inversion found.

## Memory Layout
- Cell 0: N (number of elements)
- Cell 1: result (inversion count)
- Cells 2-9: temporary variables
- Cells 10-15: array elements a[0]-a[5]
- Cells 20-25: comparison workspace
- Cells 30-35: validity flags (which array positions are populated)

## Algorithm
1. Read N and N single-digit numbers into array
2. Compute validity flags for each array position
3. For all 15 possible pairs (i,j) with i<j (up to 6 elements):
   - Check if element j is valid (exists)
   - Copy both elements to workspace
   - Use simultaneous decrement to determine if a[i] > a[j]
   - If so, increment result counter
4. Output result as 1-2 digit decimal number (divmod by 10)

## Code length
9203 characters
