# X10 -- String Rotation Check (Brainfuck)

## Approach

Uses an interleaved stride-4 memory layout to store S1 and S2 characters
in adjacent cells, enabling efficient pair-wise comparison.

### Memory Layout

- Cell 0: sentinel (always 0, used for pointer navigation)
- Cell 1: found flag (nonzero if a matching rotation was found)
- Cell 2: rotation counter (initialized to string length n)
- Cell 3: temporary / mismatch accumulator
- Data blocks at cell 4+4k: a[k] (S1), b[k] (S2), t1[k] (temp), t2[k] (temp)

### Algorithm

1. Read S1 into a-slots (cells 4, 8, 12, ...) until newline.
2. Count length n by walking a-values into cell 2.
3. Read exactly n chars of S2 into b-slots using the count as a loop control,
   avoiding EOF detection issues.
4. Re-count length into cell 2 for rotation loop.
5. Rotation loop (n iterations):
   a. Compare all (a[k], b[k]) pairs using non-destructive subtraction.
      Set t2[k] = 1 for each mismatch.
   b. Accumulate mismatches into cell 3 using the save-scan-restore pattern.
   c. If cell 3 == 0 (perfect match), increment found flag.
   d. Rotate a-values left by 1 using a bubble-swap technique:
      move a[0] to temp, then bubble it rightward through t1 cells
      while shifting all other a-values left by one position.
   e. Decrement rotation counter.
6. Output "yes" if found flag is set, "no" otherwise, using if-else BF pattern.

### Key BF Techniques

- Sentinel navigation: Cell 0 is always 0, enabling `<<<<[<<<<]` to reliably
  return to the header from any data position.
- Save-scan-restore: To access header cells from variable data positions,
  temporarily zero out the current a-value, scan left to cell 0, perform
  the header operation, scan right to the zero (our position), and restore.
- Bubble rotation: Instead of complex array shifting, bubble the first
  element through adjacent positions using t1 cells as relay stations.
- Non-destructive comparison: Copy-subtract-restore pattern using two
  temp cells per position to compare without destroying operands.
- Count-based S2 reading: Uses S1's length to read exactly n characters,
  avoiding the need to detect both newline and EOF termination.

## Evidence (Test Results)

All 6 specification tests passed.

## Difficulty Assessment

Extra Hard. Requires string rotation checking in BF, involving reading two
strings, comparing under all rotations, and in-place array rotation using
only local cell operations.
