from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79 12345678"))
catalog.append(Smartphone("Samsung", "Galaxy A33", "+79 23456789"))
catalog.append(Smartphone("Google", "Pixel 5", "+79 34567890"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79 45678901"))
catalog.append(Smartphone("Xiaomi", "Mi 10", "+79 56789012"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")