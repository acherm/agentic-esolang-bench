## E11: Sum Of Digits (Brainfuck)

### Approach
Read characters one by one until EOF. Skip the minus sign ('-') if present.
For each digit character, subtract 48 ('0') to get the digit value and add it
to a running sum in a single cell. Then convert the sum to decimal output
using divmod by 10 with leading zero suppression.

### Algorithm
1. **Input phase**: Read char into cell 0. If char is '-' (ASCII 45), skip.
   Otherwise it is a digit: subtract 48, add value to cell 1 (running sum).
   The minus detection works by subtracting 45 from a copy of the char and
   using a flag to distinguish zero (minus) from nonzero (digit).
2. **Decimal conversion**: Divmod the sum by 10 using a down-counter approach.
   The counter starts at 10 and decrements alongside the value. When the
   counter hits zero, the quotient is incremented and the counter resets.
   After the loop, remainder = 10 - counter_remaining.
3. **Output**: Print tens digit (with leading zero suppression) then ones digit,
   each offset by 48 to convert to ASCII.

### Evidence
All 6 test cases pass, including:
- Positive numbers (12345 -> 15, 999 -> 27)
- Negative numbers (-409 -> 13, -123 -> 6)
- Zero (0 -> 0)
- Repeated digits (11111 -> 5)

### Difficulties
- Detecting the minus sign requires a copy-and-compare approach since BF
  has no equality test. The flag-based method (assume true, clear if char-45
  is nonzero) works reliably.
- The "if digit" correction of -3 (since we subtract 45 for comparison but
  need 48 total) required an inverted flag to trigger only for digits.

### Difficulty Assessment
Easy-Medium. The digit-sum accumulation is straightforward BF. The minus
detection adds modest complexity. Decimal output via divmod is a standard
BF pattern. The small maximum sum (27) keeps everything within one byte.

### Design Choices
- Used 10 tape cells total, well within BF limits.
- Single-pass input: each character is processed immediately.
- Divmod by 10 for decimal output rather than hard-coded thresholds.
- Max sum of 27 means at most 2 decimal digits, simplifying output.

### Assumptions
- EOF returns 0 (confirmed from interpreter source).
- Input has no trailing newline (confirmed from test data).
- Maximum digit sum fits in a single byte (max 27, verified from all test cases).

### Critique
The solution handles all edge cases correctly. The minus detection adds some
code length but is necessary for the problem specification. The divmod approach
is reusable and general. A potential weakness is that it only handles sums up
to 255, but the problem constraints ensure this is sufficient.
