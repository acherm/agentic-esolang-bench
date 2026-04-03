# M14: Second Largest Distinct Number (Brainfuck)

## Problem
Read N followed by N integers. Output the second largest distinct value.

## Approach
1. All values stored with +128 offset to handle negative numbers (range -128..127 maps to 0..255)
2. Parse each signed integer: detect minus sign, accumulate decimal digits, compute offset value
3. Track max1 (largest) and max2 (second largest) in offset space:
   - If value > max1: max2 = max1, max1 = value
   - If value < max1 and value > max2: max2 = value
   - If value == max1: skip (distinct values only)
4. Convert max2 back to signed decimal and output

## Tape Layout
- Cell 0: input char / temp
- Cell 1: sign flag
- Cell 2: number magnitude
- Cell 3: offset value (val+128)
- Cell 4: max1 (largest, offset)
- Cell 5: max2 (second largest, offset)
- Cells 6-30: temporaries for comparison and arithmetic

## Code Size
11827 characters

## Test Results
All 6 test cases pass.
