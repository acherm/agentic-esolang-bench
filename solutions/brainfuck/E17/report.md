# E17 – Uppercase String (Brainfuck)

## Approach
For each character read from input, check if it is a lowercase ASCII letter
(value in range 97-122). If so, subtract 32 to convert to uppercase. Otherwise
output as-is.

### Range check technique
To check if a character c is in [97, 122]:
1. Compute work = c - 97 (mod 256)
2. Check if work < 26 using a simultaneous countdown:
   - Set counter = 26, flag = 1 (assume lowercase)
   - While work > 0:
     - If counter > 0: decrement both work and counter
     - If counter == 0: clear flag (not lowercase), break
   - After loop: flag indicates whether char was lowercase

### BF if/else pattern
The "if counter > 0 / else" is implemented using:
- Copy counter to a temp cell
- Use the temp as a one-shot loop for the "if true" branch
- Use a separate "not_did" flag (initially 1, cleared in if-true) for the else branch

## Tape layout
- Cell 0: input char / main loop control
- Cell 1: output copy
- Cell 2: work copy (c - 97)
- Cell 3: counter (26)
- Cell 4: flag (is_lowercase)
- Cell 5: temp for copies
- Cell 6: did_decrement temp
- Cell 7: not_did_decrement (else flag)
- Cell 8: temp2

## Design choices
- Used `,[ ... ,]` loop structure (read-first, re-read at end)
- EOF returns 0, which naturally terminates the loop
- Cells wrap mod 256, which makes the subtraction of 97 work correctly for
  values < 97 (they wrap to 159-255, all >= 26)

## Assumptions
- Input is a single line of printable ASCII (no null bytes within input)
- EOF returns 0 (confirmed by interpreter source)
- 8-bit wrapping cells (confirmed: mod 256)

## Difficulty assessment
Medium. The core challenge is implementing a range check in BF, which requires
careful orchestration of multiple cells for the comparison loop with proper
if/else branching.

## Critique
- The code could be shorter with a more cleverly packed tape layout
- The comparison loop copies the counter every iteration, adding overhead
- For very long inputs, the step count per character is proportional to
  the character value (up to ~122 iterations for the countdown), which is
  acceptable for typical inputs
