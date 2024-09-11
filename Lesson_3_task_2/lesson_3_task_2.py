from smartpfone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy S21", "+79773766946") 
phone2 = Smartphone("Apple", "iPhone 11", "+79773766945")
phone3 = Smartphone("Xiomi", "Mi 11", "+79773756946")
phone4 = Smartphone("Google", "Pixel 6", "+79883766946")
phone5 = Smartphone("OnePlus", "9 Pro", "+79663766946")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")