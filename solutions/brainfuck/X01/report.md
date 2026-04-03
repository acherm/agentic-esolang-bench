# X01 Prime Factorization - Brainfuck Solution

## Problem
Read a positive integer N > 1. Output its prime factorization as space-separated primes in ascending order with repetition.

## Algorithm
Trial division: for each d starting at 2, while N > 1:
- Compute N mod d and N / d using the standard BF divmod algorithm
- If d divides N: output d (space-separated), set N = N/d (try same d again)
- Else: increment d

## Implementation
- Decimal input: reads ASCII digits until EOF (char 0), accumulates N = N*10 + digit
- Division: standard BF divmod [->-[>+>>]>[+[-<+>]>+>>]<<<<<]
  Layout: c[i]=n, c[i+1]=d, three zeros -> c[i]=0, c[i+1]=d-r, c[i+2]=r, c[i+3]=q
- Decimal output: divmod(d, 10) to extract tens and ones digits, print as ASCII
- Compact memory layout: 10 cells (c0=N, c1=d, c2=space_flag, c3-c9=workspace)

## Code size
900 characters of BF
