with open('wew_3.txt') as f:
    lines = f.readlines()
cashes = []
for line in lines:
    name, cash = line.split(' - ')
    cashes.append(int(cash))
    if int(cash) < 20000:
        print(line, end=' ')
print('\n Средняя зарплата: ', sum(cashes) / len(cashes))