# H15: Tape Walk Final Position — Brainfuck Solution

## Approach
- **Phase 1 (Input):** Read characters one at a time. For each 'L' (ASCII 76), increment L_count. For each 'R' (ASCII 82), increment R_count.
- **Phase 2 (Cancellation):** Simultaneously decrement R_count and L_count while both are positive. The remaining nonzero count gives the magnitude; which count remained determines the sign.
- **Phase 3 (Output):** If magnitude is 0, output "0". Otherwise, output "-" if negative, then convert magnitude to decimal using divmod (÷100 then ÷10) and output digits with leading-zero suppression.

## Evidence
All 6 test cases pass.

## Difficulties
- **Signed arithmetic in BF:** 8-bit cells can't natively represent negative numbers. Solved by tracking R and L counts separately and computing magnitude + sign after cancellation.
- **Decimal output:** Divmod in BF is nontrivial. Used the standard BF divmod algorithm: decrement both value and divisor-counter simultaneously, resetting counter and incrementing quotient when counter hits 0.
- **Zero detection:** BF has no equality operator. Used the NOT pattern (set flag=1, clear if nonzero) throughout.
- **Leading zero suppression:** Needed for correct multi-digit output (e.g., "6" not "006").

## Difficulty Assessment
Medium-hard. The core logic (count L/R, determine sign/magnitude) is straightforward, but decimal output with sign handling in BF is a significant implementation challenge.

## Design Choices
- Separate R/L counters rather than offset encoding — avoids the hard problem of detecting sign from a single 8-bit cell.
- Simultaneous cancellation loop (decrement both while both > 0) for correctness.
- Standard divmod algorithm using a divisor-counter cell with reset.
- Reused cells across phases to keep tape layout compact.

## Assumptions
- Input contains only 'L' and 'R' characters (no whitespace or other chars).
- Total moves < 128 (limited by 8-bit cell size for magnitude tracking).
- EOF returns 0 (confirmed by testing the interpreter).

## Critique
- The solution is long (~2500+ BF characters) due to the decimal output routine. A more compact approach might use modular arithmetic tricks.
- The simultaneous cancellation loop is O(min(R,L)) iterations, each requiring multiple cell operations — not optimal but correct.
- Limited to magnitudes < 128. For larger inputs, would need multi-cell arithmetic.
- The divmod by 100 is unnecessary for the given test range (max 6) but provides generality up to 127.
