# H03: Count Primes Up To N -- Brainfuck Solution

## Algorithm
Trial division with sqrt optimization:
1. Parse decimal integer N from stdin (EOF = 0 terminates input)
2. For each k from 2 to N:
   - Set is_prime = 1, i = 2, i_squared = 4
   - While is_prime AND i_squared <= k:
     - Compute k mod i using the counting method (cycle counter)
     - If k mod i == 0: mark as composite
     - Increment i, update i_squared += 2*i - 1
   - If still prime: increment count
3. Output count as decimal string (up to 3 digits with leading zero suppression)

## Key optimizations
- sqrt(k) bound on trial divisors: reduces worst case from O(k) to O(sqrt(k)) divisors per number
- Early exit: inner loop stops as soon as a divisor is found
- Efficient modulo via counting: cycle a counter from I down to 0, resetting remainder each cycle

## Cell layout (20 cells)
- 0: N, 1: K, 2: COUNT, 3: I, 4: IS_PRIME, 5: INNER_CTR (unused), 6: ISQ
- 7: MOD_K, 8: MOD_I, 9: MOD_REM, 10-16: temporaries, 17-19: output digits

## Performance
- N=100: ~2.5s (well within 10s timeout)
- Code length: 2692 BF instructions
