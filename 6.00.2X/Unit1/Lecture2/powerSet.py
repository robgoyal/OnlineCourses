def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """

    N = len(items)

    for i in range(3 ** N):

        bags = ([], [])
        for j in range(N):
            if (i >> j) % 2 == 0:
                bags[0].append(items[j])
            elif (i >> j) % 2 == 1:
                bags[1].append(items[j])

        yield bags


for i in yieldAllCombos(["a", "b"]):
    print(i)
