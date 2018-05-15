def mult(a):
        def mult2(b):
            return a*b
        return mult2

print(mult(6)(2))

mult_2=mult(3)
print(mult_2(2))
print(mult_2(3))
print(mult_2(4))
print(mult_2(5))
print()

mult_4=mult(4)
print(mult_4(2))
print(mult_4(3))
print(mult_4(4))
print(mult_4(5))