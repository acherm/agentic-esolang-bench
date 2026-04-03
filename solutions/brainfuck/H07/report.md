# H07: Longest Common Prefix - Brainfuck Solution

## Approach
- Store prefix in cells 1..N contiguously
- For each subsequent string, compare character by character (unrolled for up to 20 positions)
- Use workspace cells (30+) for input buffering, backups, and flags
- Three-way branching per character: EOF, newline, or regular char
- Non-destructive prefix comparison using backup cell
- On match: continue to next position
- On mismatch: truncate prefix, skip rest of line
- Output remaining prefix at end

## Generated code: 65534 BF characters
