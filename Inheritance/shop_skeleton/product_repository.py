from project.animal import Product
from typing import List


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])