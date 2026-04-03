# X20 - Josephus Problem (Brainfuck)

## Problem
Read integers N and K. N people stand in a circle numbered 1 to N.
Starting from person 1, count K people clockwise and eliminate that person.
Repeat until one remains. Output the survivor's original number.

## Algorithm
Iterative Josephus formula:
- pos = 0
- for i = 2 to N: pos = (pos + K) mod i
- result = pos + 1 (1-indexed)

## BF Implementation Details
- Multi-digit decimal input parsing (N and K separated by space)
- Divmod algorithm for modular arithmetic: [->-[>+>>]>[+[-<+>]>+>>]<<<<<]
  Layout: n d 0 0 0 0 -> 0 ? remainder quotient 0 0
- Multi-digit decimal output with leading zero suppression
- Memory layout: cell0=N, cell1=K, cell2=i, cell3=pos, cells 4-15=scratch

## Verification
All test cases pass.
