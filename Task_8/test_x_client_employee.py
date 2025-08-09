import requests
import random
from EmployeeClass import EmployeeClass

# Список фамилий
fam = ["Пупкин", "Иванкин", "Радионов", "Шпаковский", "Куницкий", "Владимирский", "Математический", "Голубкин"]
# Список имен
names = ["Волон де Морт", "Хагрит", "Буратино", "Игнат", "Вальдемар", "Гарри", "Рон", "Джек"]
# Список статусов
status = [True, False]

# Генерация случайной фамилии
random_fam = random.choice(fam)
# Генерация случайного имени
random_name = random.choice(names)
# Генерация случайного статуса
random_status = random.choice(status)

base_url = "http://5.101.50.27:8000"

api = EmployeeClass("http://5.101.50.27:8000")
# id конкретной компании
id_comp = 3

# получить данные о сотруднике по ID
def test_get_employee_by_id():
    id_empl = 61
    resp = requests.get(base_url+'/employee/info/'+str(id_empl))
    body = resp.json()
    assert resp.status_code == 200
    assert body["first_name"] == "Сваггер"

def test_get_employee_list():
    # получить список всех сотрудников в конкретной компании
    full_list = api.get_employee_list(id_comp)
    assert len(full_list) > 0

# создание сотрудника
def test_add_new_employee():
    # получить список всех сотрудников в конкретной компании
    resp = requests.get(base_url+'/employee/list/'+str(id_comp))
    full_list = resp.json()
    len_before = len(full_list)

    # создать нового сотрудника в компании
    my_first_name = random_name
    my_last_name = random_fam
    my_middle_name = "Отчество"
    my_company_id = "3"
    my_email = "user@example.com"
    my_phone = "9379992"
    my_birthdate = "1989-06-01"
    my_is_active = True

    result = api.create_employee(first_name=my_first_name, last_name=my_last_name, middle_name=my_middle_name, company_id=my_company_id, email=my_email, phone=my_phone, birthdate=my_birthdate, is_active=my_is_active)
    new_name = result["first_name"]

    # получить количество сотрудников в компании после создания 1 сотрудника
    full_list = api.get_employee_list(id_comp)
    len_after = len(full_list)
    # проверить, что стало плюс 1
    assert len_after-len_before == 1
    # проверить, что имя нового сотрудника совпадает с назначенным
    assert new_name == my_first_name

    # проверить описание последнего (добавленного) сотрудника
    assert full_list[-1]["first_name"] == my_first_name
    assert full_list[-1]["last_name"] == my_last_name

    # изменение информации о сотруднике с ID = 1
def test_patch_employee():
    employee_id = 1
    patch_last_name = random_fam
    patch_email = "user@example.com"
    patch_phone = "9379992"
    patch_is_active = random_status

    result = api.patch_employee(employee_id, last_name=patch_last_name, email=patch_email, phone=patch_phone, is_active=patch_is_active)
    new_last_name_employee = result["last_name"]
    new_status_employee = result["is_active"]

    # проверить, что изменения прошли успешно
    assert new_status_employee == patch_is_active
    assert new_last_name_employee == patch_last_name

    # запуск кода - pytest test_x_client_employee.py