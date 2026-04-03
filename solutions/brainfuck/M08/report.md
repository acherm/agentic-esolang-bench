# M08 - Nth Fibonacci Number (Brainfuck)

## Problem
Read integer N >= 1, output F(N) where F(1)=1, F(2)=1, F(3)=2, ...

## Approach
- Parse decimal input (up to 2 digits) into a binary counter N
- Use decimal digit arrays (6 digits) for arbitrary-precision arithmetic
- Iterative Fibonacci: a=0, b=1, repeat N-1 times: t=a+b, a=b, b=t
- Carry detection via parallel decrement (subtract min(value, 10) from value)
- Output: print decimal digits from most significant, skipping leading zeros

## Code size
8660 characters of Brainfuck
