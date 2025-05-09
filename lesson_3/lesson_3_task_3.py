from address import Address
from mailing import Mailing

from_address = Address(111111, "Kazan", "Gogol str", 1, 1)
to_address = Address(222222, "Moscow", "Pusnkin str", 2, 2)

mailing = Mailing(from_address, to_address, 5000, 9999)

print(f"Отправление {mailing.track} из {from_address.index}.{from_address.city}.{from_address.street}."
     f"{from_address.block}-{from_address.apartment} в {to_address.index}.{to_address.city}."
      f"{to_address.street}.{to_address.block}-{to_address.apartment}. Стоимость {mailing.cost} рублей.")
