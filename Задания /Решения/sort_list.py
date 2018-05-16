import random

def time(func):
    def wrapper(*args):
        from time import time
        start = time()
        a = func(*args)
        end =  time()
        print('Time {}ms'.format((func.__name__,round(end-start,6))))
        return a
    return wrapper

@time
def generate_list(a, b, c):
    list_ = [random.randint(b, c) for _ in range(a)]
    list_ = sorted(list_)[::-1]
    return list_


listOne = generate_list(10000, 1, 20000000)
listTwo = generate_list(1000000, 1, 5000)
@time
def f():
    l_new = listOne+listTwo
    l_new.sort
    return l_new


# l_new2 = listOne+listTwo


@time
def bubble(list_):

    for i in range(len(list_)):
        for j in range(len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[j]
    return list_


@time
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
    #print(len(newList))
    return newList

# bubble(l_new2)
# list_of_two(listOne, listTwo)
# print(list_of_two(listOne, listTwo))
f()