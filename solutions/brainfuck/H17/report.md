# H17: Most Frequent Value

## Approach
- **Algorithm**: Frequency array with shuttle-based increment, unrolled scan for max
- **Complexity**: O(V_max) for freq array build per value, O(V_scan * N) for scan
- **BF Code Size**: 42266 characters

## Technique
1. Parse N and each value using decimal digit parsing
2. Build frequency array using stride-2 shuttle with trail markers
   - Even cells: shuttle track, Odd cells: freq[v]
   - Walk right: `[-[->>+<<]+>>]`, walk back: `<<[-<<]`
3. Unrolled scan (v=0..50): for each value, move freq to working area,
   compare with best count using safe parallel decrement (handles 8-bit wrapping)
4. Print result as decimal with leading zero suppression

## Cell Layout
- Cells 0-17: working area (N, VAL, CHAR, temps, bestV, bestC)
- Cell 20+: stride-2 frequency array (even=track, odd=freq)
