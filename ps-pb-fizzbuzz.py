# Программа выводит сумму чисел из диапазона от 1000 до 20000 включительно, 
# которые делятся и на 3 и на 5
import os

os.system('cls')


result = 0
for i in range(1001,20001):
    if (i % 3 == 0) and (i % 5 == 0):
        result += i
print(str(result))
        