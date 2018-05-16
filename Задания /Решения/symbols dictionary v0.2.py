stroka = 'aaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjb' \
         'aaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjb' \
         'aaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjb' \
         'aaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjb' \
         'aaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjbaaasssertyuioghfdkyuiouyfdcvbnbvcxzsdfghdsaFGHJDSZFGHJKasdfhjkjtrfghjb'


def test_f_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        end = time.time()
        name = func.__name__
        print('Func {} time={} '.format(name, round(end-start, 6)))
        return a
    return wrapper


@test_f_time
def count_1(stroka):
    count1 = {}
    while True:
        try:
            count1[stroka[0]] = stroka.count(stroka[0])
            stroka = stroka.replace(stroka[0],'')
        except:
            break
    return count1


@test_f_time
def count_2(stroka):
    count2 = {}
    for i in range(len(stroka)):
        count2[stroka[i]] = stroka.count(stroka[i])
    return count2


print(count_1(stroka))
print(count_2(stroka))