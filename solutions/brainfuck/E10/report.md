# E10: Sum From 1 To N — Brainfuck Solution

## Approach
Iterative accumulation with decimal digit representation.

### Algorithm
1. **Parse input**: Read ASCII decimal digits character by character, building N = N*10 + digit. Handle EOF (char 0) and newline (char 10) as terminators.
2. **Accumulate sum**: Loop from N down to 1. Each iteration, add the current N to a 4-digit decimal accumulator (ones, tens, hundreds, thousands cells), then carry-propagate using divmod-by-10.
3. **Output result**: Print the decimal digits from most significant to least significant, suppressing leading zeros. The ones digit is always printed (covers N=0 case).

### Evidence
- All 6 provided test cases pass: N=0,1,3,5,10,100 with sums 0,1,6,15,55,5050.
- The solution correctly handles the tricky N=100 case (sum=5050), which requires 4 decimal digits and exceeds a single byte.

### Difficulties
- **Multi-byte arithmetic**: Sum of 1..100 = 5050 exceeds the 0-255 range of a BF cell. Solved by using 4 separate cells as decimal digit accumulators (ones, tens, hundreds, thousands).
- **Divmod by 10 in BF**: BF has no comparison operators. Implemented using a countdown counter: count down from 10 on each unit transferred; when counter hits 0, increment quotient and reset.
- **Input parsing**: Detecting EOF vs newline vs digit characters required a multi-flag approach. Subtract 10 first (checking for newline), then subtract 38 more for the digit value.
- **Leading zero suppression**: Used a "started" flag to track whether any nonzero digit has been output; always output the ones digit.

### Difficulty Assessment
Medium-high. The core algorithm (iterative summation) is simple, but BF implementation requires:
- Decimal digit accumulator with carry propagation (divmod by 10)
- Multi-character decimal input parsing with EOF/newline detection
- Flag-based conditional execution (no if-else in BF)
- Leading zero suppression on output

### Design Choices
- **Decimal accumulator vs binary**: Chose decimal digit cells (each 0-9) to avoid binary-to-decimal conversion at output time. This trades more complex addition (carry propagation) for simpler output.
- **4-digit accumulator**: Sufficient for N up to 22 (sum=253 fits 3 digits) and N=100 (sum=5050 needs 4 digits). Could extend to more digits if needed.
- **Iterative vs formula**: Used the iterative loop (sum += N; N--) rather than N*(N+1)/2 to avoid multiplication and division of large numbers.

### Assumptions
- BF cell size is 8-bit (0-255) with wrapping arithmetic.
- EOF on input returns 0.
- Input consists of ASCII digit characters optionally followed by a newline.
- N is non-negative and fits in a single byte (N <= 255, though test cases go up to 100).

### Critique
- Code is long (~2000+ BF characters) due to the verbose nature of BF decimal arithmetic.
- The divmod-by-10 carry propagation runs 3 times per iteration (for 3 carry boundaries), making the inner loop relatively slow for large N.
- A formula-based approach (N*(N+1)/2) would be faster but harder to implement in BF due to multi-byte multiplication and division.
