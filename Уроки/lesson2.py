'''
if 1>2:
	print ("True")
else:
	pass# Нельзя оставить оператор else пустым, если ничего не нужно делать, нужно написать pass! 
	#print ("Folse")
print ("Goodbaye")
'''

'''
a= int(input("First"))
b= int(input("Second"))
if a>b:
	print ("max a,a")
else:
	print ("max b")
print ("Goodbaye")
'''

'''
a= int(input("First"))
#b= int(input("Second"))
if a>0:
	print ("positive,a")
else:
	if a==0:
		print ("Вы ввели 0")
	else: 
		print ("negative")
print ("Goodbaye")

'''


# 0 появляеися реже, чем дпугие числа, по этому его стоит опускать вниз, чтоб он не вычислялся первы а последним, это повлияет на улучшение производительности в больших программах.

'''
a= int(input("First"))
if a>0:
	print ("positive,a")
elif a<0: # Ноль- тоже является отрицательным числом 
	print ("negative")
		#print ("Вы ввели 0")
else: 
	print ("Вы ввели 0")	
print ("Goodbaye")
'''

'''
a= input("First\n")
if a.isdigit():
	#a=int(a)- если нам данное значение используется только один раз, то можно привести число к int ниже и сделать это только один раз
	if int(a)>0:
		print ("Ok") 
	else:
		print(")))")	
		
print ("Goodbaye")
'''

'''
a= int(input("First"))
print (a) #Если ввести не число, то произойдет исключение, которое необходимо  отработать!
'''
'''
try:#Пытается сделать какое то дйствие
	a= int(input("First\n"))
	print (a) #Если ввести не число, то произойдет исключение, которое необходимо отработать!
except:#Если придыдущее действие приводит к ошибке, то выполняется следующее
	print("Ввели не число")
'''
'''
try:#Пытается сделать какое то дйствие
	a= int(input("First"))
	print (a) #Если ввести не число, то произойдет исключение, которое необходимо их отработать!
except:#Если придыдущее действие приводит к ошибке, то выполняется следующее
	print("Ввели не число")
if a>0:
	print("положительное ")
Ошибка не отработается из за того, что if>0: находится в основном телле программы 	
'''
'''
a= input("Вводи\n")
try:
	a= int(a)
	print ("int",a) 
except:	
	try:
		a= float(a)
		print ("float",a)
	except:
		print("Не число")
if a:
	print("OK")	#будет выполнятся если а!=0
else:
	print("Ups")#если а равно 0 то выведется Ups 	
'''

'''
print(int(True))#True всегда является "1"
'''
'''
a= input("Вводи\n")
print(a==True)#Если ввести строку, то будет False потому что строка не равна числу и не может быть равна "1"( то же, что и true) 
print("a=",a,type(a))#выводит класс переменной
'''



'''
a=0
if a>0:
	if a%2==0:
		if a%3==0:
			print("OK")


if a>0 and not a%2 and not a%3:#другая запись верхних 5 строк
	print("Ok")
'''	
'''
a=int(input("Enter a "))
b=4
if a==0 and b==int(input("Enter ")): #вторая операция не выполнится, если первая вернет folse
	print("True")
else:
	print("Folse") 
	
'''
'''
a=0	
b=4
c=int(input("Enter\n "))
if a==0 and b==c:
	print("True")
else:
	print("Folse")

'''
#of a==0 and c==(b=int(input("Enter")))#выдас ошибку потому что в момент операции сравнения невозможна операция присвоения (синтаксис языка Python) 







