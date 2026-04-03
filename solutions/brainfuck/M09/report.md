# M09: Decimal To Binary (Brainfuck)

## Problem
Read a non-negative integer N in decimal. Output its binary representation without leading zeros (except print 0 when N = 0).

## Algorithm
1. Parse decimal input: Read ASCII digits, accumulate value = value * 10 + digit in a single cell (0-255 range).
2. Divide by 2 repeatedly (8 rounds): Use toggle-based divmod: decrement value while toggling a remainder cell (0/1); each toggle-to-0 increments the quotient. Store each remainder in a dedicated cell (cells 20-27, LSB first).
3. Output MSB first, skip leading zeros: Scan from bit 7 (cell 27) to bit 0 (cell 20). Use a started flag; output only after seeing the first 1-bit. If the value was 0, output a single 0.

## Tape Layout
- c0: accumulated value / division workspace
- c1-c3: temps for parsing and divmod
- c4: started flag for output
- c5-c8: temps for output logic
- c20-c27: stored bits (LSB at c20, MSB at c27)

## Code Size
3494 characters

## Test Results
All 6 test cases pass.
