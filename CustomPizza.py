# CustomPizza.py
from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        Pizza.__init__(self, size)
        self.toppings = []

        if self.getSize() == "S":
            self.setPrice(8.0) 
        if self.getSize() == "M":
            self.setPrice(10.0)
        if self.getSize() == "L":
            self.setPrice(12.0)

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.getSize() == "S":
            self.setPrice(self.getPrice() + 0.5)
        if self.getSize() == "M":
            self.setPrice(self.getPrice() + 0.75)
        if self.getSize() == "L":
            self.setPrice(self.getPrice() + 1)
            

    def getPizzaDetails(self):
        toppings_str = ""
        
        for item in self.toppings:
            toppings_str += f"\t+ {item}\n"
            
        if len(toppings_str) != 0:
            return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n{toppings_str}Price: ${self.price:.2f}\n"

        else:
            return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\nPrice: ${self.price:.2f}\n"


