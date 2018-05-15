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
def f(a,b):
    i = 1
    for j in range(a,b+1):
        i*=j
    return i


@time
def f1():
    i = 1
    j = 1
    #print(i)
    while j<10000:
        i*=j
        j+=1
    return i


f(10,100)
f1()

expression = input()
print(eval(expression))

#exac

#a = [1,2,3,4]
#b = [10,20,30,40]

#c=zip(a,b)
#print(c)

#for i,j in zip(a,b):
 #   print(i,j)
