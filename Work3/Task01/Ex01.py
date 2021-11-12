import json
import os
from datetime import date


class Ticket:
    def __init__(self, idn, price):
        self.id = idn
        self.price = price

    def __str__(self):
        return f"Ticket number: {self.id}\nCost: {self.price}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, idn):
        if not isinstance(idn, int):
            raise TypeError("Wrong type of data")
        if idn < 0:
            raise ValueError("Hash number cannot be negative")
        self.__id = idn

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong type of data")
        if price < 0:
            raise ValueError("Value cannot be negative")
        self.__price = price


class AdvanceTicket(Ticket):
    def __init__(self, idn, number):
        super().__init__(idn, number)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong type of data")
        if price < 0:
            raise ValueError("Value cannot be negative")
        self.__price = price * 0.6


class StudentTicket(Ticket):
    def __init__(self, idn, number):
        super().__init__(idn, number)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong type of data")
        if price < 0:
            raise ValueError("Value cannot be negative")
        self.__price = price * 0.5


class LateTicket(Ticket):
    def __init__(self, idn, number):
        super().__init__(idn, number)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Wrong type of data")
        if price < 0:
            raise ValueError("Value cannot be negative")
        self.__price = price * 1.1


class Event:
    __price = 0
    __id = 0

    def __init__(self, ticket_num, price, event_time=None):
        self.filename = "Work3/tickets.json"
        self.limit = ticket_num
        self.price = price
        self.event_time = event_time

    def create_ticket(self, students=False):
        if os.stat(self.filename).st_size > 0:
            with open(self.filename, 'r') as file:
                listdict = json.load(file)
                self.__id = max(listdict[-1]["_Ticket__id"], self.__id)
        if self.__id == 10:
            raise OverflowError("Limit reached.")
        idn = self.__id_get()
        if students:
            ticket = StudentTicket(idn, self.price)
        elif (self.event_time - date.today()).days >= 60:
            ticket = AdvanceTicket(idn, self.price)
        elif 10 <= (self.event_time - date.today()).days < 60:
            ticket = Ticket(idn, self.price)
        else:
            ticket = LateTicket(idn, self.price)
        listobj = []
        if os.stat(self.filename).st_size > 0:
            with open(self.filename, 'r') as file:
                listdict = json.load(file)
                for i in listdict:
                    t = Ticket(0, 0)
                    lists = list(i.values())
                    t.id = lists[0]
                    t.price = lists[1]
                    listobj.append(t)
        listobj.append(ticket)
        with open(self.filename, 'w') as file:
            json.dump(listobj, file, default=lambda o: o.__dict__, indent=4)

    def get_ticket(self, index):
        ticket = Ticket(0, 0)
        list_ticket = json.load(open(self.filename, 'r'))
        lists = list(list_ticket[index].values())
        ticket.id = lists[0]
        ticket.price = lists[1]
        return ticket

    def __id_get(self):
        self.__id += 1
        return self.__id

    @property
    def event_time(self):
        return self.__event_time

    @event_time.setter
    def event_time(self, event_time):
        if not isinstance(event_time, date):
            raise TypeError("Not a date instance.")
        if event_time < date.today():
            raise ValueError("Invalid date.")
        self.__event_time = event_time

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, ticket_num):
        if not isinstance(ticket_num, int):
            raise TypeError("Not an int.")
        if ticket_num <= 0:
            raise ValueError("Not a positive number.")
        self.__limit = ticket_num

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Not a number.")
        if price < 0:
            raise ValueError("Negative number.")
        self.__price = price


party = Event(10, 30, date(2022, 2, 1))
party.price = 30
party.create_ticket()
obj = party.get_ticket(-1)
print(obj)
