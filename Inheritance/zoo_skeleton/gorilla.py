from project.product_repository import Mammal


class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)