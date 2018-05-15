def f(arg): # Рекурсия
    yield arg
    arg+=1
    yield arg
    arg += 1
    yield arg
    arg += 1

a = f(100)
print(next(a))
print(next(a))
print(next(a))
''''''

def run():
    print('run')
def go():
    print('go')
def eat():
    print('chav-vhav')


a = {}
a['run'] = run
def error():
    print('Error')


if __name__ == '__main__':
    com = input()
    a.get(com,error)()