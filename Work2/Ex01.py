class Rectangle:
    def __init__(self, leng=1, wid=1):
        if not isinstance(leng, (int, float)) or not isinstance(wid, (int, float)):
            raise TypeError()

        if 20 > leng > 0 and 20 > wid > 0:
            raise ValueError()
        self.length, self.width = leng, wid

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width


def main():
    cube = Rectangle()
    reg = Rectangle(4, 2)
    print(f"'cube' instance\nPerimeter : { cube.perimeter() }\nArea : { cube.area() }\n")
    print(f"'reg' instance\nPerimeter : { reg.perimeter() }\nArea : { reg.area() }\n")
    try:
        reg = Rectangle("1", "h")
    except TypeError as e:
        print("Error.Rectangle sides must be in length of 0 to 20!\n")
    try:
        reg = Rectangle(0, -4)
    except ValueError as e:
        print("Error.Invalid types of data entered in class instance.\n")


main()
