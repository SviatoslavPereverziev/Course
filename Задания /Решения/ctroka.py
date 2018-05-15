str_ = input("Введите строку->")
x = len(str_)
if x % 2 == 0:
    a = int(x/2)
    str1 = str_[:a]
    str2 = str_[a:]
    print(str1)
    print(str2)
else:
    a = int(x / 2)
    str1 = str_[0:a+1]
    str2 = str_[a+1:]
    print(str1)
    print(str2)