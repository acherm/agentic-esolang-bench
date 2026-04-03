# M16 — Interleave Two Strings (Brainfuck)

## Solution
```
>>,----------[++++++++++>,----------]<[<]>[.,.>]
```
Length: 48 characters

## Algorithm
1. Read S1 into tape cells 2, 3, 4, ... until newline (detected by subtracting 10).
2. Navigate back to cell 2 (start of S1).
3. For each S1 character: output it, then read and output one S2 character, advance right.
4. Loop exits when we hit the 0 sentinel past end of S1.

## Tape Layout
- Cell 0–1: unused (cell 1 serves as left boundary marker, always 0)
- Cells 2..N+1: S1 characters (then 0 sentinel)
- During Phase 2, S2 characters are read into the same cells (overwriting S1 after output)

## Key Insight
Since both strings are equal length, we can output each S1[i] from memory,
then immediately read S2[i] from stdin and output it, advancing the pointer.
The `,` instruction overwrites the cell, so no clearing is needed.

## Code Breakdown
- `>>` — move to cell 2
- `,----------` — read first char, subtract 10 (newline check)
- `[++++++++++>,----------]` — if not newline: restore char, move right, read next, subtract 10; repeat
- `<[<]>` — scan left to find cell 1 (0), then right to cell 2
- `[.,.>]` — output S1 char, read+output S2 char, advance; repeat until 0 sentinel
