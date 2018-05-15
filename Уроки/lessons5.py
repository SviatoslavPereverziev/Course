'''
list_ = [1, 2, 3]
list_.append(list_)  # обект с бесконечностью, добавляет сам семя в конец бесконечое число раз
print(list_)
print(list_[-1])
for item in list_:
    print(item)
    if type(item) == list:
        for i in item:
            print(i)
    if isinstance(item, list):  # то же самое, что и 7 строчка
        for i in item:
            print(i)
'''
'''
a = [1, 2, 3, 4, 5,[77, 88, 99]]
b = a.copy()  # если написать a=b то в b будут храниться ссылки на а а не копироваться список  
b[0] = "abc"
print(a)
print(b)
'''
'''
import copy
import deepcopy 
a = [1, 2, 3, 4, 5,[77, 88, 99]]
b = deepcopy(a) # если написать a=b то в b будут храниться ссылки на а а не копироваться список
b[0] = "abc"
print(a)
print(b)
'''
'''
str_ =("ababababab")
str_.replace("a", "c")
str_two = str_.replace("a", "c")
print(str_) # выведет ababababab потому что строки не изменяются, их нужно перезаписывать
print(str_two)
list_ = [1, 67, 4, 3564, 4]
a = list_.sort()
a = sorted(list_)  # верхня строчка не работает
print(list_)
print(a)
'''
'''
a=print
a(print("Hello, World"))
'''
'''
def test():
    print("Test")

test()
'''
