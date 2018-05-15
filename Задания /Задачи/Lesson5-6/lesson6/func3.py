import random
a=[]
for _ in range(10):
    a.append(random.randint(1,100))
b = [random.randint(1,100) for _ in range(10) ]
c = [i for i in range(100)]
d=[]
for i in range(100):
    if i%2==0:
        d.append(i)
e = [i for i in range(100) if i%2==0]
z = [[j for j in range(5)] for i in range(5) ]

x = [ i for i in range(5) for j in range(i)]

y = [i if i%2 else 0 for i in [random.randint(1,100) for _ in range(10)]]
print(y)
