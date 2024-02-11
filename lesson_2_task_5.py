# Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

def month_to_season(num):
    num = int(num)
    if num >= 9 and num <= 11:
        print('Осень')
    elif num >= 3 and num <= 5:
        print('Весна')
    elif num >= 6 and num <= 8:
        print('Лето')
    else:
        print('Зима')

month_to_season(6)