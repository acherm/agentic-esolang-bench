# E14: Repeat String N Times — Brainfuck Solution

## Approach
The solution reads an integer N (potentially multi-digit) from the first line and a string S
from the second line, then outputs S repeated N times.

### Tape Layout
- Cell 0: N (repeat count, parsed from decimal input)
- Cell 1: 0 (sentinel, naturally zero after parsing)
- Cells 2..K: String characters (all nonzero printable ASCII)
- Cell K+1: 0 (string terminator from EOF)

### Algorithm
1. **Parse N**: Read decimal digits, building N = N*10 + digit for each digit.
   Multiplication by 10 uses a temporary cell. Stop at newline (ASCII 10).
2. **Read string**: Read characters into consecutive cells starting at cell 2.
   EOF naturally produces 0, terminating the string.
3. **Navigate back**: Scan left through nonzero string chars to sentinel (cell 1),
   then left one more to N (cell 0).
4. **Output loop**: While N > 0: skip past sentinel to string start (cell 2),
   print each char moving right until terminator, scan left back to sentinel,
   move to N, decrement.

## Evidence
All 6 test cases pass, including N=0 (empty output), N=1, and multi-character strings.

## Difficulties
- Multi-digit N parsing requires multiplication by 10 in BF, implemented via
  cell transfer with 10x amplification: `[-<<++++++++++>>]`
- Navigation between the repeat counter and string requires sentinel-based scanning.
- EOF behavior (sets cell to 0) was verified and relied upon for string termination.

## Difficulty Assessment
Medium. The core loop is straightforward, but decimal parsing and tape navigation
add complexity. The sentinel-based scanning pattern is elegant and avoids position tracking.

## Design Choices
- Used cell 1 as a natural sentinel: it holds 0 after the newline-detection loop exits,
  requiring no explicit initialization.
- String is stored contiguously with a 0 terminator, enabling simple `[.>]` output.
- Multi-digit N is handled via the standard multiply-accumulate pattern.

## Assumptions
- String characters are all nonzero (printable ASCII). Verified by problem description
  (string examples use letters and digits).
- EOF on `,` returns 0 (verified with the interpreter).
- N is a non-negative integer in decimal.

## Critique
- The multiply-by-10 approach works but would overflow for large N values (cells are
  typically 8-bit in many BF implementations). The test cases use small N values (0-5),
  so this is not an issue here. The interpreter likely uses wrapping arithmetic.
- No newline is output after the repeated string, matching the expected outputs.
