# X14: Next Greater Element - Brainfuck Solution

## Problem
Read an integer N followed by N integers. For each element, find the first element to its right that is greater than it. Output N integers where each is the next greater element, or -1 if none exists.

## Approach
- Parse ASCII input (N, then N space-separated numbers)
- Store array in cells 0,2,4,6,8 (up to 5 elements)
- For each element i, scan right through j=i+1..N-1
- Use simultaneous decrement comparison to check arr[j] > arr[i]
- Output result as ASCII decimal, or "-1" if no greater element found
- Space-separated output

## Implementation Details
- BF code generated programmatically via Python BFBuilder class
- Cell layout: array in cells 0-9 (even cells), N at cell 20, workspace at 21-36
- Dynamic array indexing via 5-case dispatch (decrement chain pattern)
- Handles multi-digit numbers (up to 2 digits) in both input and output
- Values range 0-10, N range 3-5

## Complexity
- O(N^2) brute force for next greater element
- Input parsing: O(N * input_length)
