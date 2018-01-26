class Food:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return "{}: <{}, {}>".format(self.name, self.value, self.calories)

    def __repr__(self):
        return self.__str__()


def maxVal(toConsider, avail):

    print(toConsider, avail)
    if toConsider == [] or avail == 0:
        result = (0, ())

    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)

    else:
        nextItem = toConsider[0]

        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()

        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))

        else:
            result = (withoutVal, withoutToTake)

    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print("Use search tree to allocate", maxUnits, "calories")
    print(foods)
    print()
    print()
    val, taken = maxVal(foods, maxUnits)

    print("Total value of items taken =", val)
    if printItems:
        for item in taken:
            print('   ', item)


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu


# names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut", "cake"]
# values = [89, 90, 95, 100, 90, 79, 50, 10]
# calories = [123, 154, 258, 354, 365, 150, 95, 195]

names = ["beer", "pizza", "burger"]
values = [90, 30, 50]
calories = [145, 258, 354]
foods = buildMenu(names, values, calories)

testMaxVal(foods, 750)
