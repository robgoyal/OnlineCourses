# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

An artificial long word said to mean a lung disease caused by inhaling very fine ash and sand dust

## According to its man page, what does `getrusage` do?

`getrusage` gets the resource usage of the system.

## Per that same man page, how many members are in a variable of type `struct rusage`?

There are 16 members in `struct rusage`.

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

Allocates stack space to create the variables in the stack frame.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

The main reads word from a file by looping through the file until it reaches the end,
checks if the character is alphabetical or contains an apostrophe, and stores the character
in the word. If the length of the word is greater than 45, it'll discard the word. If the character
is a digit, it'll discard the word. If its not an alphabetical character, apostrophe, or a number,
it means we've found a whole word, and it checks if that word is mispelled.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

`fscanf` might read in a word that's longer than what we want to store which can result in errors if our buffer isn't of enough size.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Prevents us from modifying the contents of those arguments.
