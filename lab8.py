import logging
import random
logging.basicConfig(filename='prog_loto.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

while  True: 
    try: #проверка типа введенных данных
        logging.info('User started program')
        
        n = int(input('Введите количества бочек: '))
        logging.info(f'Users input {k}')
        
    except ValueError:
        print ('Вы ввели некорректное значение. Повторите попытку')
        logging.error('Incorrect number')
        continue
    
    if n <= 0:
        print ('Вы ввели некорректное значение. Повторите попытку')
        logging.error('Incorrect number')
        continue
        
    numbers = []
    while len(numbers) != n: #программа выводит числа по не дойдет до n
        number = random.randint(1,n)
        
        if number not in numbers:
            numbers.append(number)
            print ('Выпавшее число: ', number)
            logging.info(f'Program printed {number}')
            input('Для получения следующего числа на бочонке нажмите "Enter"')
    
    print ('Выпавшие номера: ', numbers)
    logging.info(f'Programm printed all numbers: {numbers}')
    break
    logging.info('Programms end')
