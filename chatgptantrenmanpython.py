"""
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
a = input("Please enter a number: ")
s = 0 
for b in range(len(a)):
    t = a[b]
    s = int(t) + s 

print(s)
"""
"""
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
a = "ali roket gibi kod yazıyor"

b = list(a.split())
longestwordinit = (b[0])
for x in b : 
    if len(x) > len(longestwordinit):
        longestword = x 

print(longestword)
"""