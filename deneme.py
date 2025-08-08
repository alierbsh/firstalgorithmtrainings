from random import randint 
nums = list(range(0, 301))

motor = 0
us_sinir = nums[-1]
alt_sinir = nums[0]
secret_number  = randint(alt_sinir,us_sinir)
a = nums[int((alt_sinir + us_sinir)/2)]
while a != secret_number:
    if a > secret_number:
        us_sinir = a
        print(f"{motor}. deneme! aranan sayi, {alt_sinir} ile {us_sinir} arasindadir.")
    elif a < secret_number:
        alt_sinir = a 
        print(f"{motor}. deneme! aranan sayi, {alt_sinir} ile {us_sinir} arasindadir.")    
    a = nums[int((alt_sinir + us_sinir)/2)]
    motor += 1 
        
motor += 1 
print(f"{motor}. deneme! you found the secret number!!! the secret number is : {a}")