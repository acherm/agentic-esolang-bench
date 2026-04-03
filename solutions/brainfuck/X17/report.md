# X17: Roman To Integer (Brainfuck)

## Approach
1. Read Roman numeral characters one at a time
2. Classify each character (I=1, V=2, X=3, L=4, C=5, D=6, M=7) using ASCII subtraction chain
3. For each character, compare its code with the previous character's code
4. If previous < current: subtract previous value from the appropriate decimal digit
5. If previous >= current: add previous value to the appropriate decimal digit
6. After the last character, add its value (always add)
7. Normalize digits: handle 8-bit underflow (255 = -1) with decimal borrow
8. Output digits, skipping leading zeros

## Key Techniques
- One-pass algorithm with previous-character lookahead
- 8-bit wrapping arithmetic for subtraction: -1 wraps to 255, detected by adding 1 and checking for 0
- Decimal digit accumulation directly (ones, tens, hundreds, thousands)
- BF zero-check pattern for character classification and value dispatch
- Cascading borrow normalization for correct multi-digit output

## Memory Layout
- Cells 0-3: decimal digit accumulators (thousands, hundreds, tens, ones)
- Cell 4: previous character code
- Cells 5-31: working temporaries for classification, comparison, and dispatch
- Cell 32: leading-zero skip flag for output
