import time


def test_f_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        end = time.time()
        name = func.__name__
        print('Func {} time={} '.format(name, round(end-start, 6)))
        return a
    return wrapper


a = [i for i in range(1000000)]
b = [i for i in range(1000000)]


@test_f_time
def q_sort(lst1, lst2):
    return sorted(lst1+lst2)

def w_sort(lst1,lst2):
    a = []
    while True:

q_sort(a,b)