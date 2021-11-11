import datetime
import json
from random import randint


class Pizza:
    def __init__(self, name, description, price):
        self.name, self.description, self.price = name, description, price

    def __str__(self):
        return f"Pizza:{self.name}\nPrice:{self.price}\nIngredients:{self.description}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong data.")
        if not name.isalnum():
            raise ValueError("Wrong characters.")
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Wrong data.")
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong data.")
        if price < 0:
            raise ValueError("Negative number")
        self.__price = price


class DishExtras(Pizza):
    def __init__(self, name, description, price, *args):
        for i in args:
            if not isinstance(i, str):
                raise TypeError("Wrong data type.")
            if not i.isalpha():
                raise ValueError("Wrong characters.")
        self.extra = list(args)
        super().__init__(name, description, price)

    def __str__(self):
        return f"Pizza:{self.name}\nPrice:{self.price}\n" + (f"Extra ingredients: {self.extra}" if self.extra else "")

    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, ext):
        if not isinstance(ext, list):
            raise TypeError("Not a list.")
        for i in ext:
            if not isinstance(i, str):
                raise TypeError("Wrong data type.")
            if not i.isalpha():
                raise ValueError("Wrong characters.")
        self.__extra = ext


class Order:
    orders_id = 0

    def __init__(self, name):
        self.name = name
        self.__id = Order.add()
        self.dishes = []

    def add_dish(self, dish):
        if not isinstance(dish, (Pizza, DishExtras)):
            raise TypeError("Wrong data type.")
        self.dishes.append(dish)

    def rem_dish(self, num):
        if not isinstance(num, int):
            raise TypeError("Wrong data type.")
        if not 0 <= num < len(self.dishes):
            raise IndexError("Out of bounds.")
        self.dishes.pop(num)

    def __str__(self):
        return f"\tYour Order:\nCustomer:{self.name}\nOrder number:{self.__id}\n\tDishes:\n" + \
               "".join(str(i) + "\n" for i in self.dishes) + f"\nTotal price:{sum(i.price for i in self.dishes)}"

    @classmethod
    def add(cls):
        cls.orders_id += 1
        return cls.orders_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong data type.")
        if not name.isalpha() and not name.isspace():
            raise ValueError("Invalid characters.")
        self.__name = name


def add_menu(name, description, price):
    pizza = Pizza(name, description, price)
    menu = json.load(open("Work3\\pizzas.json", 'r'))
    pizzalist = []
    for i in menu:
        temp = Pizza("0", "0", 0)
        temp.__dict__ = i
        pizzalist.append(temp)
    pizzalist.append(pizza)
    json.dump(pizzalist, open("Work3\\pizzas.json", 'w'), default=lambda o: o.__dict__, indent=4)


file = open("Work3\\pizzas.json", 'r')
lists = json.load(file)
pizzas = []
for j in lists:
    t = Pizza("0", "0", 0)
    t.__dict__ = j
    pizzas.append(t)
file.close()

entity = json.load(open("Work3\\date.json", 'r'))
if entity[1] != datetime.date.today().weekday():
    file = open("Work3\\date.json", 'w')
    entity[1] = datetime.date.today().weekday()
    pizza = pizzas[randint(0, len(pizzas)-1)]
    while entity[0] == pizza.__dict__:
        pizza = pizzas[randint(0, len(pizzas)-1)]
    entity[0] = pizza
    json.dump(entity, file, default=lambda o: o.__dict__, indent=4)
    file.close()
pizza_of_day = Pizza("0", "0", 0)
pizza_of_day.__dict__ = entity[0]
print(f"Pizza of the day:\n{pizza_of_day}")

while True:
    response = input("What is your name?:")
    try:
        order = Order(response)
        break
    except ValueError as e:
        print(e, "Must contain letters. Try again.\n\n")
iterable = 1
while iterable:
    while iterable:
        for j in range(len(pizzas)):
            print(f"{j}.{pizzas[j]}")
        response = input("Choose the dish ('q' to quit):")
        try:
            if response == 'q' and iterable != 1:
                iterable = 0
            elif response == 'q':
                print("Order at least 1 dish to finish the order.\n")
            elif range(len(pizzas)).__contains__(int(response)):
                iterable += 1
                break
            else:
                print("Out of list bounds. Choose a correct number\n")
        except ValueError as e:
            print("Not a number. Please try again\n")

    while iterable:
        obj = pizzas[int(response)]
        extra = []
        while True:
            response = input("Add Extra ingredients ('q' to quit):")
            if response == "q":
                break
            extra.append(response)
        try:
            order.add_dish(DishExtras(obj.name, obj.description, obj.price, *extra))
            break
        except ValueError as e:
            print("Invalid extra ingredient entered. Please try again.\n")
print(order)
