class Product:
    """
    Instance of Class contains data about the product:
    description, price and dimensions. Class contains method,
    that converts all info about the product into string.
    """
    def __init__(self, des="", prc=0, wid=0, length=0, hgt=0):
        if not (isinstance(des, str) and isinstance(prc, int) and isinstance(wid, int) and isinstance(hgt, int) and
                isinstance(length, int)):
            raise TypeError("Invalid type of data was entered.")
        if prc < 0 or wid < 0 or hgt < 0 or length < 0:
            raise ValueError("Value cannot be negative.")
        self.description, self.price, self.width, self.length, self.height = des, prc, wid, length, hgt

    def print_product(self):
        return f"   {self.description}\nPrice:{self.price}\nDimensions:{self.width} X {self.length} X {self.height}\n"


class Customer:
    """
    Instance of Class contains data about customer:
    full name and phone number. Class contains method,
    that converts all info about customer into string.
    """
    def __init__(self, name, surname, patronymic, phone):
        if not (isinstance(name, str) and isinstance(surname, str) and
                isinstance(patronymic, str) and isinstance(phone, str)):
            raise TypeError("Invalid type of data was entered.")
        if not phone.isdigit():
            raise ValueError("Not a phone number was entered.")
        self.name, self.surname, self.patronymic, self.phone = name, surname, patronymic, phone

    def print_custom(self):
        return f"NSP:{self.name} {self.surname} {self.patronymic}\nPhone number:{self.phone}"


class Order:
    """
    Instance of Class contains instance of Customer class and
    list of instances of Product class. Class contains method to
    add or remove Product instances from the list. Method Total
    returns total price of products. Method 'print_order' returns
    string with information about customer and each order.
    """
    products = []

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("No customer data was entered.")
        self.customer = customer

    def add_product(self, des, prc, wid, length, hgt):
        self.products.append(Product(des, prc, wid, length, hgt))

    def rem_product(self, ind):
        if not isinstance(ind, int):
            raise TypeError("Invalid type of data was entered.")
        self.products.pop(ind)

    def total(self):
        return sum(i.price for i in self.products)

    def print_order(self):
        return f"{self.customer.print_custom()}\n" + "".join(i.print_product() for i in self.products) +\
               f"\nTotal order value:{self.total()}"


def main():
    form = Order(Customer("Dasha", "Symonenko", "Andriivna", "0971001122"))
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
