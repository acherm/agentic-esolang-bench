# X06: Compute Power Modulo (B^E mod M) - Brainfuck Solution

## Algorithm
Modular exponentiation via repeated modular multiplication:
- result = 1
- Loop E times: result = (result * B) mod M
- Modular multiplication: product = 0; loop B times: product = (product + result) mod M

## Implementation Details
- Two-byte (base-256, little-endian) arithmetic for values up to 1000
- Memory layout: B (cell 0), E (cell 1), M (cells 2-3), result (cells 4-5), product (cells 6-7), B_counter (cell 8), temps (cells 9+)
- Addition uses increment-by-1 with zero detection for carry
- Modular reduction uses speculative subtraction: subtract M, then check hi-byte range to detect underflow, rollback if needed
- Output uses digit extraction by repeated subtraction of 100 and 10, with leading zero suppression
- BF code length: 9156 characters
