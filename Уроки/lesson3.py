'''
while True:
	try:
		a=int(input("->"))
	except:
	
		print("Только числа") 
print("Ура, ты молодец!")

'''
'''
a=int(input("->"))
summ=0
while a!=-44:
	summ+=a
	a = int(input("-->"))
	print(4)
print("Результат",summ)

'''
'''
a=int(input("->"))
summ=0

while a!=-44:
	if a:
    	summ=1/a
		a = int(input("-->"))

print("Результат",summ)
'''
'''
summ=0

while True:
	try:
		a = int(input("-->"))
	except:
		continue
	if a==-44:
		break
	if a:
		summ+=1/a

print(summ)
'''
'''
i=0
summa=0
while i<3:
	a=int(input("->"))
	summa+=a
	i+=1
	print("i=",i)
print("i=",i,"summa",summa)
print("End")
'''
'''
for i in range(10,2,-2):
    print(i)
'''
'''
i = 0
summa = 0

for i in range(3):
    summa += int(input("->"))
'''
'''
summa = 0
a = range(3)

for i in a:
    print(i)
'''
'''
a = [1, 2, 3, 10, 12]
for i in a:
    print(i)
'''
'''
Не работало!!! Посмотреть дома:
a = [1, 2, 3, 10, 12]
for i in a:
	i=-77
    print(i)
print("After loop",a)
'''
'''
a = [1, 2, 3, 10, 12, 3, 23, 234, 2, 5, 745, 345, 2]
print("Длинна", len(a))  # длинна
print(a[2])  # вывод i-го элемента
for i in a:
    print(i)
print("After loop", a)
'''
'''
a = [1, 2, 3, 10, 12]
print("Длинна", len(a))  # длинна
str_ = "j"
print("Длинна", len(str_))


for letter in str_:
    #print(a[0])
    #print(str_[-1])
    print(a)
    a[0]=0
    print(a)
'''
'''
a = [1, 2, 3, 10, 12]
#print("Длинна", len(a))
str_ = "jdfgdfgfd"
#print("Длинна", len(str_))

print(str_[3:6])  # срез, для того чтоб выводить определенные элементы от одного, до следующего ч шагом
print(str_[::-1])  # реверс строки 
'''
'''
a, b = input("Числа через пробел ").split()
print(a,b)
'''




