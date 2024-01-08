# PizzaOrder.py
from Pizza import Pizza

class PizzaOrder(Pizza):
    def __init__(self, time):
     #   Pizza.__init__(self, time)
        self.pizzas = []
        self.time = time
        
    def setTime(self, time):
        self.time = time
        
    def getTime(self):
        return self.time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        total_order = "******\nOrder Time: " + str(self.getTime()) + "\n"
        price = 0

        for item in self.pizzas:
            total_order += item.getPizzaDetails() + "\n" + "----\n"
            price += item.getPrice()
        return total_order + f"TOTAL ORDER PRICE: ${price:.2f}\n******\n"

