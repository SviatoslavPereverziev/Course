import random


def generate_list(a, b, c):
    list_ = [random.randint(b, c) for _ in range(a)]
    list_ = sorted(list_)[::-1]
    return list_


listOne = generate_list(50, 1, 2000)
listTwo = generate_list(50, 1, 5000)


def list_of_two(listOne, listTwo):
    newList = []

    if len(listTwo) >= len(listOne):
        longList = listTwo
        shortList = listOne
    else:
        longList = listOne
        shortList = listTwo

    for i in range(len(shortList) + len(longList)):
        try:
            if shortList[0] <= longList[0]:
                newList.append(longList[0])
                longList.pop(0)

            elif shortList[0] > longList[0]:
                newList.append(shortList[0])
                shortList.pop(0)

        except IndexError:
            if len(longList) != 0:
                for _ in range(len(longList)):
                    newList.append(longList[0])
                    longList.pop(0)

            elif len(shortList) != 0:
                for _ in range(len(shortList)):
                    newList.append(shortList[0])
                    shortList.pop(0)
    print(len(newList))
    return newList


print(list_of_two(listOne, listTwo))
