from project.booths.booth import Booth


class PrivateBooth(Booth):
    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = 3.50 * number_of_people
        self.is_reserved = True