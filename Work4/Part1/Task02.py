class Product:
    def __init__(self, name, quantity, price, *args, **kwargs):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Info: {self.name}\n\tQuantity: {self.quantity}\n\tPrice: {self.price}"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.quantity, self.price) == (other.name, other.quantity, other.price)

    def __ne__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.quantity, self.price) != (other.name, other.quantity, other.price)

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.quantity > other.quantity
        elif isinstance(other, int):
            return self.quantity > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Product):
            return self.quantity >= other.quantity
        elif isinstance(other, int):
            return self.quantity >= other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.quantity < other.quantity
        elif isinstance(other, int):
            return self.quantity < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Product):
            return self.quantity <= other.quantity
        elif isinstance(other, int):
            return self.quantity <= other
        else:
            return NotImplemented

    def copy(self):
        return Product(self.name, self.quantity, self.price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'unsupported type(s) for \'name\' as {type(name).__name__}')
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError(f'unsupported operand type(s) for {type(quantity).__name__}')
        if quantity < 0:
            raise ValueError(f'unsupported value(s) of {quantity}')
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError(f'unsupported operand type(s) for {type(price).__name__}')
        if price < 0:
            raise ValueError(f'unsupported value(s) of {price}')
        self.__price = price


class Composition:
    def __init__(self, *args):
        self.composition = list(*args)

    def available(self, name):
        if not self.__contains__(name):
            return f"{name}: Not available"
        temp = self.__getitem__(name)
        return f"REPORT:\n{temp.name}: {'Available' if temp.quantity > 0 else 'Not available'}"  # temp.quantity

    def available_all(self):
        return f"REPORT:\n" + "".join(f'{i.name}:' + ('Available\n' if i.quantity > 0 else 'Not available\n')
                                      for i in self.composition)

    def __str__(self):
        return "COMPOSITION:" + "".join(f"\n\n\t{i}" for i in self.composition)  # f

    def __getitem__(self, item):
        if isinstance(item, str):
            if not any(item == i.name for i in self.composition):
                raise ValueError(f'no item(s) of {item} found')
            return next(i for i in self.composition if item == i.name)
        elif isinstance(item, int):
            return self.composition[item]
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(item).__name__}')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not isinstance(value, Product):
            raise TypeError(f'unsupported type(s) of {type(key).__name__} or {type(type(value).__name__)}')
        self.composition.__setitem__(key, value)

    def __contains__(self, item):
        if not isinstance(item, str):
            return NotImplemented
        return any(item == i.name for i in self.composition)

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        temp = [i.copy() for i in self.composition]
        temp.append(other)
        return Composition(temp)

    def __iadd__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        self.composition.append(other)

    def __sub__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        if not any(other == i.name for i in self.composition):
            return NotImplemented
        temp = [i.copy() for i in self.composition]
        temp.remove(next(i for i in temp if other == i.name))
        return Composition(temp)

    def __isub__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        if not any(other == i.name for i in self.composition):
            return NotImplemented
        self.composition.remove(next(i for i in self.composition if other == i.name))

    def __eq__(self, other):
        if not isinstance(other, Composition):
            return NotImplemented
        return self.composition == other.composition

    def __ne__(self, other):
        if not isinstance(other, Composition):
            return NotImplemented
        return self.composition != other.composition

    @property
    def composition(self):
        return self.__composition

    @composition.setter
    def composition(self, composition):
        if not composition:
            self.__composition = []
        else:
            if not isinstance(composition, list):
                raise TypeError(f'unsupported type(s) of {type(composition).__name__} for "composition"')
            if len(composition) > 0 and not all(isinstance(i, Product) for i in composition):
                raise ValueError(f'unsupported value(s) of {type(composition).__name__} for "composition"')
            self.__composition = composition


test = Composition()
test = test + Product("Pen", 25, 5)
test = test + Product("Bike", 10, 5000)
print(test)
test = test - "Pen"
print(test)
print(test.available_all())
print(test[0])
print(test["Bike"])
print("Bike" in test)
print(test == test)
