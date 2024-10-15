from project.animal import Product


class Food(Product):
    def __init__(self, name: str):
        self.quantity = 15
        super().__init__(name, self.quantity)