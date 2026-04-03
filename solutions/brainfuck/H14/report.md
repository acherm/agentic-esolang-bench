# H14 - List All Divisors (Brainfuck)

## Algorithm
1. Parse decimal input N
2. Compute floor(N/2) using toggle counter
3. For i from 1 to floor(N/2): check N mod i == 0, output i if so
4. Always output N as last divisor (N always divides itself)

## Mod Algorithm
Counting approach: countdown from I, reset when reaching 0.
Divisibility flag set on each reset, cleared each iteration.
After N iterations, flag = 1 iff N mod I == 0.
Zero-check uses move-test-restore pattern.

## Optimizations
- Only check candidates up to N/2 (all proper divisors are <= N/2)
- This halves candidate count and cuts total BF operations significantly
- Handles N=1 through N=255 within timeout

## Code Size
2713 characters of Brainfuck.
