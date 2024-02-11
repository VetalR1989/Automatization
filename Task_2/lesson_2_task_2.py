# Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе.

is_year_leap = input("Введите год: ")
is_year_leap = int(is_year_leap)
if (is_year_leap % 4 == 0):
    print ("Год " + str(is_year_leap) + ": True")
else:
    print ("Год " + str(is_year_leap) + ": False")