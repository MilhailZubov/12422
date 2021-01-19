with open("wew.txt", "w") as f:
    while True:
        str_1 = input('Введите строки: ')
        if str_1 == '':
            break
        f.write(str_1 + "\n")