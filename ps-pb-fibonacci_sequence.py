# Программа анализа последовательности Фибоначи,
# состоящую из чисел, которые меньше 10.000.000 (десять миллионов)
import os

os.system('cls')


fib1 = 1
fib2 = 1
fib = 0
sum_of_even_elements = 0
number_of_elements = 2
even_elements = []

# Вычисление и анализ последовательности Фибоначи.
while (fib + fib2) < 10000000:
    fib = fib1 + fib2
    fib2 = fib1
    fib1 = fib
    if fib % 2 == 0:# Проверка на четность элемента последовательности Фибоначи.
        even_elements.append(fib)# Добавление в список четного элемента.
        sum_of_even_elements += fib# Суммируем четные элементы.
    number_of_elements += 1

print ("Количество элементов в последовательности = " + str(number_of_elements))
print ("Сумма всех четных элементов = " + str (sum_of_even_elements))

print ("Все четные элементы: ", end=" ")
for i in even_elements:
   print (i, end= " ")

print ("")
print ("Предпоследнее число последовательности = " + str(fib2))  
