a = 0
b = []
def fun1():
    #global a
    a = 1
    b.append(a)
    def fun2():
        #nonlocal a
        a=2
        b.append(a)
        def fun3():
            #global a
            a=3
            b.append(a)
            def fun4():
                #nonlocal a
                #global a
                a=4
                b.append(a)
                print('Local fun4', a)

            fun4()
            print('Local fun3', a)

        fun3()
        print('Local fun2', a)

    fun2()
    print('Local fun1', a)

fun1()
b.append(a)
print('Global',a)
print('Список', b)
