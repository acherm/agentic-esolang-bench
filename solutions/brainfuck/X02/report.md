# X02 - Longest Increasing Subsequence Length (Brainfuck)

## Algorithm
O(n^2) DP approach:
- dp[i] = length of LIS ending at position i
- dp[i] = 1 + max(dp[j] for j < i where A[j] < A[i])
- Answer = max(dp[i])

## Implementation
- ASCII decimal number parser handling multi-digit numbers
- Unrolled outer/inner DP loops (up to 10 elements)
- Comparison routines (less-than, greater-equal) using simultaneous decrement
- Global max tracking
- ASCII decimal output (handles 1-10)

## Tape Layout
- Cells 0-13: workspace (N, number parsing)
- Cell 14: saved N
- Cell 16: global max (answer)
- Cells 50-69: array storage (value/dp pairs, stride 2)
- Cells 80-87: comparison workspace
- Cells 90-91: output workspace
