#  Программа согласование числительных множественного числа.
import os

os.system('cls')


def plural_form(number,noun1,noun2,noun3):
    """Функцию согласования окончаний существительных в зависимости от переданного числа.
    :param number: число от которго будет зависеть окончание существительного.
    :param noun1,noun2,noun3: существительные подходящие под определенное число.
    """
    if (number == 1):
        print(f'{number} {noun1}')
    elif ((number == 2) or  (number == 3) or (number == 4)):
        print(f'{number} {noun2}')
    elif (number >= 5):
        print(f'{number} {noun3}')
    
plural_form(1,"яблоко","яблока","яблок")
plural_form(2,"яблоко","яблока","яблок")
plural_form(11,"студент", "студента", "студентов")
plural_form(15,"студент", "студента", "студентов")
plural_form(3,"студент", "студента", "студентов")
