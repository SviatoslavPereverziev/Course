stroka = input('Введите текст->',)
count = {}

for i in range(len(stroka)):
    count[stroka[i]] = stroka.count(stroka[i])

print(count)