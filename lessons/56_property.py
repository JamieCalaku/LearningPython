# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height


    # Getter method
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Setter method
    @width.setter
    def width(self, new_width):
        self._width = new_width

    @height.setter
    def height(self, new_height):
        self._height = new_height

    # Deleter method
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)

print()

rectangle.width = 5
rectangle.height = 6

print()

print(rectangle.width)
print(rectangle.height)

print()

del rectangle.width
del rectangle.height