# Создание класса Address

class Address:

    def __init__(self, indeks, city, street, house, apartment):
        self.indeks = indeks
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

        # print(self.indeks, self.city, self.street, self.house, "-", self.apartment)
        
    def __str__(self):
        return (f"{self.indeks}, {self.city}, {self.street}, {self.house} - {self.apartment}")