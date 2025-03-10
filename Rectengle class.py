class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def values(self):
        return f"Length = 20\n Width = 10"
    def area(self):
        return f"Area = {self.length*self.width}"
    def perimeter(self):
        return f"Perimeter = {2*(self.length+self.width)}"
shape = Rectangle(20,10)
print(shape.values())
print(shape.area())
print(shape.perimeter())
