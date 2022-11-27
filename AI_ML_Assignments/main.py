"""
Python function to count the ODD & EVEN numbers within N natural Numbers
"""
from tokenize import String


def countODDaEVEN(num):
    if num % 2 == 0:
        print("Number of ODD numbers are : " + str(num // 2))
        print("Number of EVEN numbers are : " + str(num // 2))
    else:
        print("Number of ODD numbers are : " + str(num // 2 + 1))
        print("Number of EVEN numbers are : " + str(num // 2))


def printPatters(num):
    i, j = 0, 0
    print("Pattern 1 : ")
    for i in range(0, num):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")

    print("Pattern 2 : ")

    k = num
    while k > 0:
        for i in range(0, k):
            print(end="  ")
        while i < num:
            print(" *", end="")
            i = i + 1
        print("\t")
        k = k - 1

    print("Pattern 3 : ")

    k = num
    while k > 0:
        for i in range(0, k):
            print(end=" ")
        while i < num:
            print(" *", end="")
            i = i + 1
        print("\t")
        k = k - 1


def Fib1(num):
    if num <= 1:
        return num
    else:
        return Fib1(num - 1) + Fib1(num - 2)


def Fib2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fib2(num - 1) + Fib1(num - 2)



countODDaEVEN(10)
printPatters(5)
print("10th fib no is : "+str(Fib1(10)))
print("10 fib no are : ",end=" ")
for i in range(0,11):
    print(Fib2(i),end=" ")
