# E13 — Maximum Of Three (Brainfuck)

## Approach
1. Parse three space-separated signed integers (A, B, C) using digit accumulation
2. Store each as sign (0=positive, 1=negative) + magnitude
3. Compare A vs B using signed comparison (handles different sign cases and same-sign magnitude comparison)
4. Compare winner vs C using the same signed comparison
5. Output result with sign handling and leading zero suppression

## Code size
11962 characters

## Tests
All 6 tests passed.
