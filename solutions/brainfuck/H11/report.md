# H11: Run Length Decoding — Brainfuck Solution

## Approach
Streaming parser: read one symbol character, then one digit character. Convert the digit from ASCII to integer (subtract 48). Output the symbol that many times by looping. Repeat until EOF.

## Tape Layout
- Cell 0: symbol character
- Cell 1: repeat count (digit - 48)

## BF Code
```
,[>,------------------------------------------------[<.>-]<,]
```

### How it works
- `,` reads the symbol into cell 0
- `[` main loop (while not EOF)
- `>,` move to cell 1, read digit character
- `------------------------------------------------` subtract 48 (ASCII '0') to get numeric count
- `[<.>-]` inner loop: output symbol (cell 0), decrement count (cell 1)
- `<,` move back to cell 0, read next symbol
- `]` loop if not EOF

## Evidence
All 6 specification tests pass:
- `a3b2` → `aaabb`
- `x1` → `x`
- `z9` → `zzzzzzzzz`
- `A2B3C1` → `AABBBC`
- `m4n2p1` → `mmmmnnp`
- `q1w1e1r1` → `qwer`

## Difficulty Assessment
Easy-medium. The streaming approach is natural for BF. The only arithmetic needed is subtracting a constant (48) from the digit character.

## Design Choices
- Single-digit counts only (1-9), so no multi-digit parsing needed
- Streaming (no need to store the entire encoded string)
- Minimal tape usage (2 cells)

## Assumptions
- EOF returns 0 (standard BF convention)
- Counts are always single digits 1-9
- Input is well-formed (alternating char-digit pairs)

## Critique
The problem is well-suited to BF's streaming I/O model. At 61 characters, this is one of the most compact solutions in the benchmark. The restriction to single-digit counts avoids the complexity of multi-digit parsing that plagues many other problems.
