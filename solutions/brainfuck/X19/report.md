# X19 - Permutation Check (Brainfuck)

## Algorithm
1. Parse N from first line (decimal, newline-terminated)
2. Parse N space-separated numbers from second line
3. Mark flag[V] for each input value V using a shuttle technique on a 2-cell-per-slot flag array
4. Check all flags 1..N: scan through flags, decrement each, normalize to 0/1, accumulate bad count
5. If bad count = 0, output "yes"; otherwise output "no"

## Key Techniques
- **Decimal parsing**: Multi-digit decimal input with EOF/newline/space detection using cascading zero-checks with guard patterns
- **Flag array shuttle**: `[[->>+<<]+>>-]` pattern to navigate to flag[V] in a 2-cell-per-slot array, with breadcrumb-based return via `<<[[-]<<]`
- **Check scan**: `[>-[>+<[-]]<<[->>+<<]>>>[-<+>]<<[->>+<<]>>-]` walks through flags 1..N with separate iteration counter and bad-flag accumulator to ensure termination

## Code size: 1600 characters
