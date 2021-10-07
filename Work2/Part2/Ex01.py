class Product:
    def __init__(self, des="", prc=0, wid=0, length=0, hgt=0):
        if isinstance(des, str) and isinstance(prc, int) and isinstance(wid, int) and isinstance(hgt, int) and \
                isinstance(length, int):
            if prc >= 0 and wid >= 0 and hgt >= 0 and length >= 0:
                self.description, self.price, self.width, self.length, self.height = des, prc, wid, length, hgt
            else:
                raise ValueError("Value cannot be negative.")
        else:
            raise TypeError("Invalid type of data was entered.")

    def print_product(self):
        return f"   {self.description}\nPrice:{self.price}\nDimensions:{self.width} X {self.length} X {self.height}"


class Customer:
    def __init__(self, name, surname, patronymic, phone):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(patronymic, str) and phone.isdigit():
            self.name, self.surname, self.patronymic, self.phone = name, surname, patronymic, phone
        else:
            raise TypeError("Invalid type of data was entered.")

    def print_custom(self):
        return f"NSP:{self.name} {self.surname} {self.patronymic}\nPhone number:{self.phone}"


class Order(Customer):
    products = []

    def add_product(self, des, prc, wid, length, hgt):
        self.products.append(Product(des, prc, wid, length, hgt))

    def rem_product(self, ind):
        if isinstance(ind, int):
            self.products.pop(ind)
        else:
            raise TypeError("Invalid type of data was entered.")

    def total(self):
        summary = 0
        for i in self.products:
            summary += i.price
        return summary

    def print_order(self):
        string = "" + self.print_custom() + '\n'
        for i in self.products:
            string += i.print_product() + '\n'
        string += "Total order value: " + str(self.total())
        return string


def main():
    form = Order("Dasha", "Symonenko", "Andriivna", "0971001122")
    form.add_product("Small cup", 10, 6, 6, 10)
    form.add_product("Pen", 1, 1, 1, 5)
    print(form.print_order(), end='\n\n')
    form.rem_product(0)
    try:
        form.add_product("NO", 'Get outta here', '0', '0', '0')
    except TypeError as e:
        print(e)
    try:
        form.add_product("NO", -3, 1, 3, 1)
    except ValueError as e:
        print(e)
    

main()
