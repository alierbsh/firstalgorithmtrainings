from random import randint 
nums = list(range(0, 301))


us_sinir = nums[-1]
alt_sinir = nums[0]
secret_number  = 2
a = int(input("please enter your number = "))
while a != secret_number:
    if a > secret_number:
        us_sinir = a
        print(f"aranan sayi, {alt_sinir} ile {us_sinir} arasindadir.")
    elif a < secret_number:
        alt_sinir = a 
        print(f"aranan sayi, {alt_sinir} ile {us_sinir} arasindadir.")    
    a = int(input("please enter your number = "))
    while a < alt_sinir or a > us_sinir : 
        print("dude, aptalca bir secim yaptin. tekrar dene.")
        a = int(input("please enter your number = "))

print(f"you found the secret number!!! the secret number is : {a}")