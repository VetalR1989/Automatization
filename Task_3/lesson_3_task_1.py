class User:
    first_name = 'No first_name'
    last_name = 'No last_name'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst_name(self):
        print(self.first_name)

    def sayLast_name(self):
        print(self.last_name)

    def sayFirst_name_Last_name(self):
        print(self.first_name + ' ' + self.last_name)