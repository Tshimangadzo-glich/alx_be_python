import math
from oop.polymorphism_demo import rectangle
from oop.polymorphism_demo import Circle
class Shape:
    def area(self):
        class Rectangle(Shape):
            def area(self):
                def __init__(self, length: float, width: float):
                    self.length = length
                    self.width = width
def area(self):
    return self.length * self.width
class Circle(Shape):
    def area(self):
        return math.p1 * (self.radius ** 2)
    if __name__ == "__main__":
                    self.rectangle = rectangle
                    self.Circle = Circle
                    rectangle = rectangle(5, 3)
                    circle = Circle(4)
                    print(f"Rectangle area: {rectangle.area()}")
                    print(f"Circle area: {circle.area()}")
if __name__ == "__main__":
    main()
