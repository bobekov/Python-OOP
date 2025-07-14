from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPE = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPE = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self._find_delicacy(name) is not None:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.DELICACY_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        new_delicacy = self.DELICACY_TYPE[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self._find_booth(booth_number) is not None:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.BOOTH_TYPE:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth = self.BOOTH_TYPE[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        not_reserved_booth = next((b for b in self.booths if not b.is_reserved), None)
        if not_reserved_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        if not_reserved_booth.capacity >= number_of_people:
            not_reserved_booth.reserve(number_of_people)
            return f"Booth {not_reserved_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._find_booth(booth_number)
        delicacy = self._find_delicacy(delicacy_name)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if self._find_delicacy(delicacy_name) is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_booth(booth_number)
        bill = sum(delicacy.price for delicacy in booth.delicacy_orders) + booth.price_for_reservation
        booth.delicacy_orders = []
        self.income += bill
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def _find_delicacy(self, name):
        delicacy = [d for d in self.delicacies if d.name == name]
        return delicacy[0] if delicacy else None

    def _find_booth(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        return booth[0] if booth else None




