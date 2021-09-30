class Rectangle:
    def __init__(self, leng=1, wid=1):
        try:
            if 20 > leng > 0 and 20 > wid > 0:
                self.length = leng
                self.width = wid
            else:
                print("Error.Rectangle sides must be in length of 0 to 20!\nDefault values set as 1.")
                self.length = self.width = 1
        except TypeError:
            print("Error. Invalid types of data entered in class instance.\nDefault values set as 1.")
            self.length = self.width = 1

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width


def main():
    cube = Rectangle()
    reg = Rectangle(4, 2)
    print(f"'cube' instance\nPerimeter : { cube.perimeter() }\nArea : { cube.area() }\n")
    print(f"'reg' instance\nPerimeter : { reg.perimeter() }\nArea : { reg.area() }\n")
    err = Rectangle("1", "h")
    print(f"err' instance\nPerimeter : {err.perimeter()}\nArea : {err.area()} \n")
    err = Rectangle(0, -4)
    print(f"err' instance\nPerimeter : {err.perimeter()}\nArea : {err.area()} \n")


main()
