## E07: String Length (Brainfuck)

### Approach
Read characters one by one until EOF (which returns 0 in this interpreter),
incrementing a counter for each character. Then convert the counter to a
decimal string and output it.

### Algorithm
1. **Counting phase**: Simple read-increment loop. Read char into cell 0,
   while nonzero increment cell 1 and read next char.
2. **Decimal conversion**: Two-stage divmod approach:
   - Divmod counter by 100 to extract hundreds digit
   - Divmod remainder by 10 to extract tens and ones digits
3. **Output**: Print digits with leading zero suppression. Hundreds printed
   only if nonzero. Tens printed if hundreds was printed or tens is nonzero.
   Ones always printed.

### Divmod Implementation
The BF divmod(V, N) uses a down-counter D initialized to N. For each
decrement of V, D is also decremented. When D reaches zero, the quotient
is incremented and D is reset to N. After the loop, remainder = N - D.

The zero-check for D uses a flag-based approach: set flag=1, copy D to
temp, if temp nonzero clear flag, then if flag is set D was zero.

### Evidence
All 6 test cases pass including edge cases (empty string -> "0",
single char, strings with spaces and special characters).

### Difficulties
- Implementing divmod in BF requires careful cell management and a
  reliable zero-check mechanism.
- Leading zero suppression needs an OR-like condition (print tens if
  hundreds was printed OR tens is nonzero), implemented by summing the
  flag and a copy of the tens digit.

### Difficulty Assessment
Medium. The counting part is trivial BF, but decimal output with leading
zero suppression requires significant BF engineering (divmod, conditionals).

### Design Choices
- Used down-counter divmod rather than repeated subtraction for cleaner
  zero detection.
- 13 tape cells used total, well within BF limits.
- Handles values 0-255 (full BF byte range) correctly.

### Assumptions
- EOF returns 0 (confirmed from interpreter source).
- Input does not contain trailing newline (confirmed from test data).
- Maximum string length fits in a single byte (0-255).

### Critique
The code is somewhat long due to the divmod machinery, but is correct
and handles all edge cases. A shorter approach might use hard-coded
subtraction thresholds, but divmod is more general and maintainable.
