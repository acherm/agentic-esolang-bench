# M01 Palindrome Check - Brainfuck Solution

## Tape Layout
- Cell 0: 255 (stopper for +[-<+] navigation ferry)
- Cell 1: flag (1=palindrome, 0=mismatch found)
- Cell 2: workspace (for output)
- Cell 3: 0 (left data sentinel)
- Cells 4..N+3: input characters
- Cell N+4: 0 (right sentinel from EOF)

## Algorithm
Shuttle-decrement palindrome checker. Compares outermost unprocessed character
pairs, working inward until all pairs match (palindrome) or a mismatch is found.

### Key steps
1. Read input into consecutive cells 4..N+3 with 0-sentinels at cells 3 and N+4
2. Main loop at R (rightmost unprocessed char):
   - Copy R to R+1 (using R+2 as temp, preserving R)
   - Navigate to L (leftmost unprocessed), add +128 bias to L
   - Shuttle: alternately decrement L and R+1 until R+1=0
   - Navigate to L, subtract 128 bias
   - If L=0: match (clear R, advance inward)
   - If L!=0: mismatch (print "no", clear flag, exit loop)
3. After loop: navigate to cell 1 via ferry, print "yes" if flag=1

### Key techniques
- `<[<]>` and `>[>]<`: find leftmost/rightmost active chars using 0-sentinels
- +128 bias on L before shuttle prevents L from reaching 0 during comparison
  (since all ASCII values are <= 127, L+128-R >= 1 always holds)
- `+[-<+]` ferry: traverses leftward through 0-cells, stopped by cell 0 (255 -> 0)
  Each cell is temporarily +1 then -1 (net unchanged). Cell 0 acts as stopper.
- Cell 0 restored to 255 after mismatch ferry for reuse by post-loop ferry

## Code size
637 characters

## Test results
All 6 problem examples passed, plus 17 additional edge cases including
21-character palindromes, non-palindromes with various mismatch positions,
single characters, two-character strings, and punctuation.
