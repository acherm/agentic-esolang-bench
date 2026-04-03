# H19: Plus Minus Reset Machine - Brainfuck Solution

## Approach

The solution reads a string of "+", "-", and "0" characters, tracking an accumulator X that starts at 0.

### Input Dispatch
Characters are dispatched by subtracting ASCII values:
- Subtract 43 ("+"): if result is 0, it was "+" -> increment POS counter
- Subtract 2 more: if result is 0, it was "-" (ASCII 45) -> increment NEG counter
- Otherwise: it was "0" (ASCII 48) -> clear both POS and NEG counters

A HANDLED flag prevents double-dispatch (critical fix: without it, clearing INPUT to 0 after handling "+" then subtracting for "-" check creates a nonzero value that triggers the fallthrough reset case).

### Sign Tracking
Instead of offset encoding (which complicates reset-to-zero), the solution uses two separate counters:
- POS: counts increments since last reset
- NEG: counts decrements since last reset
- Reset operation: clear both counters

### Output
After input processing:
1. Subtract min(POS, NEG) from both via simultaneous decrement loop
2. If NEG > 0: print "-" sign, move NEG to POS
3. Print POS as unsigned decimal using divmod-by-10 (twice for up to 3 digits)
4. Leading zero suppression for hundreds and tens digits

## Evidence
- All 6 provided test cases pass
- 16 additional edge cases pass including: single characters, 3-digit values (100, 123, 127, 200, 255), negative values up to -200, multiple resets, alternating +/-, empty accumulator scenarios

## Difficulties
- **Character dispatch in BF**: The main difficulty was implementing if-else-if dispatch. The initial version had a critical bug where handling "+" cleared INPUT to 0, then subtracting 2 for the "-" check created 254 (8-bit wrap), which fell through to the "0" (reset) handler. Fixed by adding a HANDLED flag that gates each subsequent check.
- **Signed decimal output**: Decomposed into sign determination (which counter is nonzero) and unsigned decimal output (divmod by 10).

## Difficulty Assessment
Medium. The core logic is simple, but BF's lack of if-else requires careful flag management. The signed decimal output with leading zero suppression adds complexity.

## Design Choices
1. **Two-counter approach** (POS/NEG) instead of offset encoding: makes the reset operation trivial (clear both cells) rather than needing to restore a specific offset value.
2. **HANDLED flag for dispatch**: ensures each character is processed exactly once, preventing cascading through subsequent character checks.
3. **Divmod-by-10 algorithm**: uses a down-counter that resets to 10, incrementing the quotient each time it hits zero. Clean and correct for any cell value 0-255.

## Assumptions
- Input contains only "+", "-", and "0" characters (ASCII 43, 45, 48)
- The final value fits in a BF cell (0-255 magnitude), sufficient for all test cases
- EOF returns 0 (standard BF behavior)
- 8-bit wrapping cells

## Critique
- Code size (1489 chars) could be reduced with more compact dispatch or by inlining the divmod, but clarity and correctness were prioritized.
- The simultaneous-decrement comparison loop is O(min(POS,NEG)), which is fine for reasonable input sizes but could be slow for very long inputs. A more efficient approach would track sign and magnitude directly, but that complicates the +/- operations.
- The solution handles values up to 255 (3 digits). Values beyond 255 would wrap due to 8-bit cells, but the problem constraints appear to keep values well within range.
