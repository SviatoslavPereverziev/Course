'''
st = ""
for _ in range (3):
    a = input("->")
    st = st+a
    print (st)
'''
-------------------------
'''
st = []
for _ in range (3):
    a = input("->")
    st.append(a)
print(st)
st = "".join(st)
print(st)
'''
'''
st = []
for _ in range (3):
    a = input("->")
    st.append(a)
print(str(st)[1:-1])#?????
st = "".join(st)
print(st)
'''
'''
st = []
st2 = []
st.append("stroka")
st2.extend("stroka")
print(st)
print(st2)
'''
'''
import random

lst_random = []
for _ in range(10):
    lst_random.append(random.randint(1,100))

print(lst_random)
'''
'''
import random

lst_random = []
for _ in range(10):
    lst_random.append(random.randint(1,100))

for elem in lst_random:
    if elem :
'''
