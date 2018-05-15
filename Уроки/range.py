import random

randomList = [i for i in
              [random.randint(1, 100000)
               for _ in range(1000)]]

endOne = [i for i in randomList if i % 10 == 1]

happyTicket = [i for i in randomList if
   (len(str(i)) == 5 and ((i//10000)+(i//1000 % 10)) == (i % 100//10+i % 10)) or
   (len(str(i)) == 4 and ((i//1000)+(i//100 % 10)) == (i % 100//10+i % 10)) or
   (len(str(i)) == 3 and i//100 == i % 10)or
   (len(str(i)) == 2 and i//10 == i % 10)]

palindromes = [i for i in randomList if
   (len(str(i)) == 5 and i // 10000 == i % 10 and i // 1000 % 10 == i % 100 // 10) or
   (len(str(i)) == 4 and i // 1000 == i % 10 and i // 100 % 10 == i % 100 // 10) or
   (len(str(i)) == 3 and i // 100 == i % 10) or
   (len(str(i)) == 2 and i // 10 == i % 10)]

print()
print("Random List", randomList)
print()
print("End One", endOne)
print()
print("happy Ticket", happyTicket)
print()
print("Palindromes", palindromes)