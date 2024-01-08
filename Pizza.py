# Pizza.py

class Pizza:
    def __init__(self, size):
        self.size = size
        self.price = 0.0
    
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size
