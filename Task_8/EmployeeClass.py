import requests

class EmployeeClass:

    def __init__(self, url):
        self.url = url

    # функция помогатор (валидация)
    def validate_employee_data(self, employee_data, required_fields):
    # Проверяет, что все обязательные поля присутствуют и не пустые
        for field in required_fields:
            if field not in employee_data or employee_data[field] in (None, '', []):
                raise ValueError(f"Поле '{field}' является обязательным и не может быть пустым.")

    # функция-помогатор
    def get_employee_list(self, id_comp, params_to_add = None):
    # получить список всех сотрудников в конкретной компании
        resp = requests.get(self.url+'/employee/list/'+str(id_comp), params=params_to_add)
        return resp.json()

    # функция-помогатор
    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active):
        employee = {'first_name' : first_name,
                    'last_name' : last_name,
                    'middle_name' : middle_name,
                    'company_id' : company_id,
                    'email' : email, 
                    'phone' : phone, 
                    'birthdate' : birthdate, 
                    'is_active' : is_active
        }
        
        # Список обязательных для создания полей
        required_fields = ['first_name', 'last_name', 'company_id']

        # Проверка обязательных полей
        self.validate_employee_data(employee, required_fields)

        resp = requests.post(self.url+'/employee/create', json=employee)
        return resp.json()

    # функция-помогатор
    def get_token(self, user = 'harrypotter', password = 'expelliarmus'):
        creds = {
            'username' : user,
            'password' : password
        }
        # авторизация
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["user_token"]

    # функция-помогатор
    def patch_employee(self, employee_id, last_name, email, phone, is_active):
        p_employee = {'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'is_active': is_active
    }


        # Обязательные поля для изменения (например, last_name и email обязательны)
        required_fields = []

        self.validate_employee_data(p_employee, required_fields)
        my_params = {}
        my_params["client_token"] = self.get_token()
        resp = requests.patch(self.url+'/employee/change/'+str(employee_id), json=p_employee, params=my_params)
        return resp.json()