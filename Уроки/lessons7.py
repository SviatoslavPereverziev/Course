

def func (obj):
    rez = obj(1,4)
    print (rez)

def f1(a,b):
    return a+b

def f2(a,b):
    return a-b

func(f2)
''''''
a=5

def f():
    a = 555
    print("local",a)

f()
print("global",a)
''''''
a=5

def f():
    global a
    if a>0:
        a = 555
    print("local", a)

f()
print("global", a)
'''''''
a=5


def f(i):
    if i>0:
        i = 555
    print("local", i)
    return i


a = f(a)
print("global", a)

''''''
НЕ РАБОТАЛА!!! РАЗОБРАТЬСЯ ДОМА!!!
def f():
    nonlocal a
    a=77
    def f1():
        global a
        a=333
        print("local in local",a)
    f1()
    print("local", a)

    def f2():
        nonlocal a
        a=555
        print("local in local f2",a)
    f1()
    f2()
a=7
f()
print("global",a)
''''''
''''''

def f():
    a=77
    def f1():
        global a
        a=333
        print("local in local",a)
    f1()
    print("local", a)

    def f2():
        nonlocal a
        a=555
        print("local in local f2",a)
    f1()
    f2()
a=7
f()
''''''
''''''


def f(name):
    def f1(b):
        return ("{}+{}".format(name,b))
    return f1
obj = f("15")
names = ["12","32","4","12","1"]
for i in names:
    print(obj(i))