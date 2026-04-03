# E04: Sum Two Integers - Brainfuck Solution

## Approach
Decimal digit array representation with 10s complement arithmetic.

Each number is stored as 7 decimal digit cells (ones to 10^6).
Negative numbers are converted to 10s complement before addition.
After addition, if the result is negative (most significant digit >= 5),
it is converted back and a minus sign is output.

## Key Design Choices
- 7-digit decimal representation (range: -5000000 to 4999999)
- 10s complement for negatives: eliminates separate add/subtract logic
- Carry detection via parallel countdown comparison
- Leading zero suppression in output
- Parsing handles sign detection and multiple terminators (EOF, space, newline, CR)

## Evidence
All provided test cases pass:
- Simple addition: 5+7=12
- Negative + positive: -3+10=7
- Zero: 0+0=0
- Three-digit: 100+200=300
- Both negative: -50+(-25)=-75
- Carry across digits: 999+1=1000

## Difficulties
- Carry detection in 8-bit cells required careful comparison logic using
  a parallel countdown approach (decrement both value copy and counter,
  detect which reaches zero first)
- 10s complement conversion with carry propagation through all digit positions
- Leading zero suppression in output requires tracking a "started" flag
- The check_ge_n function must not permanently modify the checked cell
  when used for sign detection (required restore logic)

## Difficulty Assessment
Hard. Multi-byte arithmetic in BF with 8-bit cells is inherently complex.
The decimal digit approach avoids binary overflow issues but requires
careful carry/borrow logic at each digit position. The 10s complement
representation elegantly unifies addition and subtraction into a single
addition operation, but requires complement conversions.

## Assumptions
- Numbers and their sum fit within the 7-digit 10s complement range
- Input format: two integers separated by whitespace (space)
- EOF returns 0 from the interpreter

## Critique
The generated code is long (30868 chars) but correct and handles all test cases.
The 10s complement approach trades code size for algorithmic simplicity:
only one arithmetic operation (addition) is needed instead of both addition
and subtraction with magnitude comparison. Code size could be reduced by
using fewer digits, but 7 provides a comfortable safety margin.
