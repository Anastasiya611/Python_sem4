# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N: '))
import math 
def prime_factors(n): 
    while n % 2 == 0: 
        print(2,) 
        n /= 2 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            print(i,) 
            n /= i 
    if n > 2: 
        print(n) 
prime_factors(n) 

