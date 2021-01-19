with open('wew_5.txt', 'w') as d:
    nummbers = input('Введите целые числа: ')
    d.write('Введенные числа: ' + nummbers+ '\n')
    nummbers = map(int, nummbers.split())
    summ = sum(nummbers)
    d.write('Сумма введенных чисел: ' + str(summ))
   # print('Сумма введенных чисел: ', summ)