# E08 - Reverse String: Brainfuck Solution Report

## Approach

The solution uses a classic Brainfuck idiom for string reversal:

```brainfuck
>,[>,]<[.<]
```

The algorithm works in three phases:

1. **Setup** (`>`): Move to cell 1, leaving cell 0 as a zero sentinel. This is
   necessary because the interpreter does not allow the pointer to go below
   cell 0, so we need a zero cell at the left boundary to terminate the
   output loop.

2. **Input phase** (`,[>,]`): Read characters into cells 1, 2, 3, ...
   advancing right after each read. When EOF is encountered (value 0), the loop
   exits and the pointer sits on the zero cell immediately after the last
   stored character.

3. **Output phase** (`<[.<]`): Move left one cell to reach the last real character,
   then enter a loop that prints the current cell and moves left. The loop
   terminates when it reaches cell 0 (the zero sentinel). Since we start from
   the rightmost character and move left, the output is the reverse of the input.

## Evidence

### Spec tests
All spec tests PASSED.

Test cases from the benchmark:
- "abcd" -> "dcba"
- "racecar" -> "racecar" (palindrome)
- "hello world" -> "dlrow olleh" (includes space)
- "a" -> "a" (single character)
- "12345" -> "54321" (digits)
- "ab" -> "ba" (two characters)

### Extra tests
All extra tests PASSED.

- "A" -> "A" (single uppercase letter)
- "AB" -> "BA" (two uppercase letters)

## Difficulties

**Difficulty assessment: Very Easy (1/10)**

This is one of the most well-known Brainfuck programs. The tape naturally serves
as a stack/array, and reading characters sequentially into consecutive cells is
the default behavior. Reversing output is simply a matter of traversing the tape
in the opposite direction.

No difficulties were encountered. The algorithm is a single line of 11 characters
and handles all edge cases naturally (empty input, single character, palindromes,
strings with spaces and digits).

## Design Choices

1. **Direct BF idiom vs. high-level generator**: The solution is short enough that
   using raw BF instructions is clearer than constructing it with BFGen's helper
   methods. The `,[>,]<[.<]` pattern is idiomatic and well-understood.

2. **EOF handling**: The interpreter returns 0 on EOF, which naturally terminates
   the input loop and serves as the sentinel for the output loop. No special
   EOF detection logic is needed.

3. **No cell initialization needed**: Cells default to 0 in Brainfuck, so cells
   beyond the input data are already zero, providing natural loop termination.

## Assumptions

- The interpreter returns 0 on EOF (standard behavior, confirmed by tests).
- Input does not contain null bytes (character value 0), as these would be
  indistinguishable from EOF.
- The tape is large enough to hold the entire input string.
- Input is a single line with no trailing newline passed to the program (the
  framework strips or does not include trailing newlines).

## Critique of the Problem

The problem is straightforward and well-specified. The test cases cover important
edge cases (single character, palindrome, spaces, digits). One potential gap is
that there is no test for empty input, which would produce empty output with this
solution. The problem is a good introductory exercise for Brainfuck as it
demonstrates the tape-as-array paradigm without requiring arithmetic or complex
control flow.
