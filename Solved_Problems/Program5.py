
#1) ==>> Modulus and Integer Division.

e = 105
f = e % 10
print(f)

g = 3
h = g % 10
print(h)

# If one number is not exactly divided by other number, then it will give quotient as floating point number
# If we want reminder as integer then we use floor division

c = 77
d = c // 10
print(d)

a = 2
b = a // 10
print(b)

RESULT:
5
3
7
0

#2) ==>> Print all the digits of a number on different lines.

n = 456
m = n
while m != 0:
    d = m % 10
    print(d)
    m = m // 10

RESULT:
6
5
4

#3) ==>> Print all the digits of a number on different lines with number as a user input.

x = int(input("Enter a number : "))
m = x
while m != 0:
    d = m % 10
    print(d)
    m = m // 10

#4) ==>> Check a number is palindrome or not.

n = 767
m = n
sum = 0
while m != 0:
    d = m % 10
    sum = sum * 10 + d
    m = m // 10
if sum == n:
    print("Yes the Number is Palindrome")
else:
    print("The Number is not a Palindrome")

RESULT:
Yes the Number is Palindrome

#5) ==>> Append List, with removing the duplicates.

box1 = [6, 7, 8, 9, 10, 11, 12, 13, 14]
box2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in box1:
    if i not in box2:
        box2.append(i)
print("List after removing Duplicates", box2)

RESULT:
List after removing Duplicates [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#6) ==>> Check a number is palindrome or not with user input.

repeat = int(input("Enter total Intervals: "))
for i in range(repeat):
    n = int(input("Enter a Number: "))
    m = n
    sum = 0
    while m != 0:
        d = m % 10
        sum = sum * 10 + d
        m = m // 10
    if sum == n:
        print("Yes the Number is Palindrome")
    else:
        print("The Number is not a Palindrome")

#7) ==>> Check a number is Spy number or not (sum of its digits is equal to product of its digits)

m = 123
sum = 0
prod = 1
while m != 0:
    d = m % 10
    sum = sum + d; prod = prod * d
    m = m // 10
if sum == prod:
    print(True, "Spy Number ")
else:
    print(False, "Not a Spy Number ")

RESULT:
True Spy Number

#8) ==>> Check a number is Special number or not (Sum of digits plus product of its digits is equal to original number)

n = 59
m = n
sum = 0
prod = 1
while m > 0:
    d = m % 10
    sum = sum + d; prod = prod * d
    m = m // 10
if (sum + prod) == n:
    print(True, "Special Number ")
else:
    print(False, "Not a Special Number ")

RESULT:
True Special Number

#9) ==>> Check a number is Niven/Harshad number or not (The given number is divided by the sum of its digits total and get a reminder zero)

n = 156
m = n
sum = 0
while m > 0:
    d = m % 10
    sum = sum + d
    m = m // 10
if n % sum == 0:
    print(True, "Niven Number ")
else:
    print(False, "Not a Niven Number ")

RESULT:
True Niven Number

#10) ==>> Check a number is Duck number or not (A Number which has zeros present in it )

n = 1506
m = n
count = 0
while m > 0:
    d = m % 10
    if d == 0: count += 1
    m = m // 10
if count > 0:
    print(True, "Duck Number ")
else:
    print(False, "Not a Duck Number ")

RESULT:
True Duck Number

#11) ==>> Check a number is Neon number or not (Where the sum of digits of square of the number is equal to the number)

n = 9
m = n * n
sum = 0
while m > 0:
    d = m % 10
    sum = sum + d
    m = m // 10
if sum == n:
    print(True, "Neon Number ")
else:
    print(False, "Not a Neon Number ")

RESULT:
True Neon Number

#12) ==>> Check a number is Automorphic number or not (It is a number which is contained in the last digits of its square)

n = 25
m = n
flag = True; q = n * n
while m > 0:
    d = m % 10; d1 = q % 10
    if d != d1: flag = False
    m = m // 10; q = q //10
if flag == True:
    print(True, "Automorphic Number ")
else:
    print(False, "Not a Automorphic Number ")

RESULT:
True Automorphic Number

#13) ==>> Check a number is Special number or not (Where sum of factorial of digits is equal to the number)

import math
n = 145
m = n
sum = 0
while m > 0:
    d = m % 10
    sum = sum + math.factorial(d)
    m = m // 10
if sum == n:
    print(True, "Special Number ")
else:
    print(False, "Not a Special Number ")

RESULT:
True Special Number

#14) ==>> Program to check Prime number or Not.

num = int(input("Enter a Number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not A Prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

#15) ==>> Program to check Prime number or Not with Repeated Intervals

times = int(input("Enter total Intervals: "))
for i in range(times):
    num = int(input("Enter a Number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not A Prime number")
                break
        else:
            print("Prime number")
    else:
        print("Not a prime number")


#16) ==>> Factorial of a Number Using For loop(Method-1)


num = int(input("Enter the number: "))
result = 1
for i in range(1, num+1):
    result = result*i
print("Factorial of", num, "is", result)


#17) ==>> Factorial of a Number Using For loop(Method-2)

num = int(input("Enter the number: "))
result = 1
for i in range(num, 0, -1):
    result = result*i
print("Factorial of", num, "is", result)


#18) ==>> Factorial of a Number Using While Loop(Method-3)


num = int(input("Enter the number: "))
result = 1
while num > 0:
    result = result*num
    num = num-1
print("Factorial of the number is", result)

#19) ==>> Factorial of a Number Using Function and For Loop(Method-4)

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

num1 = int(input("Enter the number : "))
result = fact(num1)
print(result)

#20) ==>> Factorial of a number by Recursive Method:

def facto(n):
    return 1 if (n == 1 or n == 0) else n*facto(n-1)
num1 = int(input("Enter the number : "))
print("factorial of", n, "is", facto(num1))

#21) ==>> Fibonacci Number (Method-1)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("enter the number: "))
for i in range(num):
    print(fibo(i))

#22) ==>> Fibonacci Number (Method-2)

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
number = int(input("enter the number: "))

fib(number)

#23) ==>> Armstrong Number In The Range of 0 to 1000(number of n digits which are equal to sum of nth power of its digit)
        #Ex1) ==>> number=5 n=1, 5 power of 1 is 5 itself
        #Ex2) ==>> number=153 n=3, (1 power of 3 + 5 power of 3 + 3 power of 3 = 1+125+27 =153(Number itself)

for m in range(1001):
    num = m
    result = 0
    n=len(str(m))
    while(m!=0):
        digit = m%10
        result = result + digit**n
        m = m//10
    if num == result:
        print(num)

#24) ==>> Reverse a Number

a = int(input("Enter a Number : "))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a //= 10
print("reversed number", rev)

#25) ==>> Reverse a string or number(Slicing Method)

name = "Albert Einstein"
print(name[::-1])

num = str(123)
print(num[::-1])

num1 = input("Enter a number : ")
print(num1[::-1])
# Here while giving a user input we have not mentioned int so it will take the number as string only, so no need of num1 = str(num1)

print(input("Enter a number : ")[::-1])

number_string = input("Enter the number : ")
number_string_reversed = number_string[::-1]
print(number_string_reversed)

#26) ==>> To check the number of Vowels and Consonants

name = input("Enter any String : ")
vowels = 0
consonants = 0
for n in name:
    if n in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels += 1
    elif n.isalpha():
        consonants += 1
print("Number of Vowels are : ", vowels, "Number of Consonants are", consonants)


# Star Program

r = int(input("Enter number of rows : "))
k = 1
n = r
for i in range(0, r):
    print(" "*n, end =" ")
    n -= 1
    for j in range(0, k):
        print("*", end=" ")
    k = k + 1
    print()

# Star program

n = int(input("Enter The Number Of Rows : "))
for i in range(1, n+1):
    print(" "*(n-i)+" *"*i)