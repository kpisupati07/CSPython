# Pizza.py
import math

class Pizza:
    def __init__(self, name, diameter, price, slices):
        self.name = name
        self.diameter = diameter
        self.price = price
        self.slices = slices

    def __str__(self):
        return f"Your {self.name} pizza has a diameter of {self.diameter} inches, a price of ${self.price}, and {self.slices} slices per pie"

    def area_per_slice(self):
        radius = self.diameter / 2
        area = math.pi * radius ** 2
        return area / self.slices

    def cost_per_slice(self):
        return self.price / self.slices

    def cost_per_square_inch(self):
        return self.cost_per_slice() / self.area_per_slice()
