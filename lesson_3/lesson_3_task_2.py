from smartphone import Smarthpone

catalog = [
    Smarthpone("Iphone", "18SuperPuper", "+7-999-111-11-11"),
    Smarthpone("Iphone", "20ProMax", "+7-999-222-22-22"),
    Smarthpone("Samsung", "Galaxy30", "+7-999-333-33-33"),
    Smarthpone("Samsung", "Galaxy100", "+7-999-444-44-44"),
    Smarthpone("Xiaomi", "20", "+7-999-555-55-55")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.phone_number}")
