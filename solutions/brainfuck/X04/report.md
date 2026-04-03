# X04: Evaluate Postfix Expression - Brainfuck Solution

## Approach
- Stack-based RPN evaluator, data pointer tracks stack top
- Input classified via subtraction chain with done-flag gating
- Operators (+,-,*,/) implemented at stack top with scratch cells
- Stack shift applied via conditional BF pointer movement
- Division uses standard BF divmod algorithm
- Output converts result to multi-digit decimal ASCII

## Code length
1983 characters
