# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
n = int(input("Введите N:"))
from random import randint
list = [randint(-10, 10) for i in range(1, n+1)]
print (list)
temp = [] 
for x in list: 
    if x not in temp: 
        temp.append(x) 
list = temp 
print(temp)
