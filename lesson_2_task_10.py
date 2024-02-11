def bank(summa, year):
    total = summa
    for i in range(year):
        total = total + (total * 0.10)
    return total
summa = int(input("Введите сумму: "))
year = int(input("Введите количество лет: "))

print(bank(summa, year))