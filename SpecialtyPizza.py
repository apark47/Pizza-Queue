# SpecialtyPizza.py
from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        self.name = name
        self.size = size

        if self.getSize() == "S":
            self.setPrice(12.0)
        if self.getSize() == "M":
            self.setPrice(14.0)
        if self.getSize() == "L":
            self.setPrice(16.0)

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
