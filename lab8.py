import logging
import random
while  True:
    try:
        n = int(input('Введите количества бочек: '))
    except ValueError:
        print ('Вы ввели некорректное значение. Повторите попытку')
        continue
    if n <= 0:
        print ('Вы ввели некорректное значение. Повторите попытку')
        continue
    numbers = []
    while len(numbers) != n:
        number = random.randint(1,n)
        if number not in numbers:
            numbers.append(number)
            print ('Выпавшее число: ', number)
            input('Для получения следующего числа на бочонке нажмите "Enter"')
    print ('Выпавшие номера: ', numbers)
    break
