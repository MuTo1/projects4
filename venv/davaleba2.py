import random
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length * self.width

    def rectangle_perimeter(self):
        return (self.length + self.width)*2

    def print_info(self):
        return f"სიგრძე -  {self.length},სიგანე -  {self.width},პერიმეტრი- {self.rectangle_perimeter()}, ფართობი - {self.rectangle_area()}"


Rectangle2 = Rectangle(8,15)
Rectangle3 = Rectangle(8,15)
r = Rectangle(8,15)
print(r.print_info())
