# X18: Integer To Roman (Brainfuck)

## Approach
- Read ASCII digits from input (EOF = 0), convert to numeric values (0-9)
- Count digits (1-4) and normalize to [thousands, hundreds, tens, ones] using flag-based switch
- Copy each digit to a workspace cell to avoid flag-cell overlap with adjacent digits
- For each digit position, use nested if/else branching to output the correct Roman numeral string

## Key Techniques
- EOF detection (returns 0) for input reading termination
- Nested if/else pattern: flag-based zero/nonzero testing for multi-way branching on digit values
- Workspace isolation: digits processed in a separate cell region to prevent clobbering
- Incremental character output exploiting ASCII proximity of Roman numeral characters
- Destructive cell moves for digit normalization based on input length

## Complexity
- Input: 1-4 ASCII digit characters
- Output: 1-15 Roman numeral characters
- BF code is verbose due to lookup table expansion but runs in O(1) time
