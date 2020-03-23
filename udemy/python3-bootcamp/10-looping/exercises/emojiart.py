# Emoji art: for loop
for i in range(1, 11):
    print("\U0001f600" * i)

# Emoji art: while loop
i = 1
while i < 11:
    print("\U0001f600" * i)
    i += 1

# Emoji art: centered pyramid
start, stop = 1, 20
for i in range(start, stop, 2):
    print((stop - i) // 2 * "  " + "\U0001f600" * i)
