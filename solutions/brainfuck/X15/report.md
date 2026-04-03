# X15: Spiral Matrix Traversal (Brainfuck)

## Approach
Generated BF code from Python that:
1. Reads R and C as single-digit values from ASCII input
2. Computes R*C via BF multiplication
3. Reads all matrix values using a "shuttle" pattern (counter walks right, values deposited behind)
4. Computes case_id = (R-1)*5 + (C-1) to identify the matrix dimensions
5. Uses a switch/case pattern to select the correct spiral order for the given dimensions
6. Outputs values in spiral order with space separators

## Key Techniques
- Shuttle pattern for reading variable number of values
- Values stored as value+1 to distinguish from empty cells (0)
- BF switch/case using flag cells and countdown
- Handles all matrix sizes from 1x1 to 5x5
