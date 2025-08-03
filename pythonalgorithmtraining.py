"""
problem 1 
palindrome check fonk
aciklama : bu motor ile girilen degerin tersten yaziminin duzden yazimina
esit olup olmadigini kontrol eden bir fonksiyondur.
def ispalindrome(text):
    return text == text[::-1]

a = input("Lütfen bir input giriniz: ")

if ispalindrome(a):
    print("This is a palindrome string.")
else:
    print("This is not a palindrome string.")
"""

""""
problem 2 
def fibonaccimotor(nnumb):
    a = 0
    b = 1 
    c = list()
    t = 0 
    for x in range(nnumb):
        t = a+b 
        c.append(t)
        a = b 
        b = t 
        return(c)

fibonaccimotor(1000)
       
"""
""""
problem 3 
a = input("Please enter a number: ")
s = 0 
for b in range(len(a)):
    t = a[b]
    s = int(t) + s 

print(s)
"""
"""
problem 4 
a = input("Please enter a number: ")
s = 1 
for t in a : 
    s *= int(t) 
print("the product of numbers variebles: ",s )
"""

"""
a = input("Please enter a number: ")
print(len(a))
"""
"""
problem 5 
a = "ali roket gibi kod yazıyor"

b = list(a.split())
longestwordinit = (b[0])
for x in b : 
    if len(x) > len(longestwordinit):
        longestword = x 

print(longestword)
"""
"""
problem 6 
from random import randint 

a = randint(1,300)
us = 300
als = 0
b= 0
while a != b :
    b = randint(als,us)
    print(f"computer guess is : {b}")
    if a == b :
        print("true guess")
    elif a > b :
        als = b  
        print(f"the number between: {als} < secretnum < {us} ")
    else:
        us = b
        print(f"the number between:{als} < secretnum < {us} ")
"""

"""
numbers = [2, 7, 11, 15]

for t in numbers: 
    for b in numbers:
        if t + b == 9 and t != b :
            a = int(numbers.index(t))
            c = int(numbers.index(b))
            print(f"{a}, {c}") 
"""
       