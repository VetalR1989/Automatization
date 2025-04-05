from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("225710", "Пинск", "Ленина", "1", "20")
from_address = Address("771102", "Париж", "Эйфеля", "2", "48")

# Создаем почтовое отправление
my_mailing = Mailing(to_address, from_address, 300, "RVV880011")


# Выводим информацию об отправлении
print(my_mailing)