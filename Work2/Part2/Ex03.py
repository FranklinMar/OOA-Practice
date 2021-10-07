import statistics
import operator


class Student:
    def __init__(self, name, surname, number, *args):
        ind = True
        for i in args:
            if not isinstance(i, int):
                ind = False
        if isinstance(name, str) and isinstance(surname, str) and isinstance(number, int) and ind:  # and not ind:
            # and isinstance(grades, list) \
            self.name, self.surname, self.number, self.grades = name, surname, number, args
            self.average = statistics.mean(self.grades)
            # self.counting()
        else:
            raise TypeError("Invalid type of data was entered.")

class Group:
    group = []
    surnames = []
    names = []

    def __init__(self, student):
        self.group.append(student)
        self.surnames.append(student.surname)
        self.names.append(student.name)

    def add_student(self, student):
        if isinstance(student, Student):
            if len(self.group) <= 20 and student.surname not in self.surnames and student.name not in self.names:
                self.group.append(student)
                self.surnames.append(student.surname)
                self.names.append(student.name)
            elif len(self.group) > 20:
                raise BufferError("Limit of students in a group reached(20).Abort creating instances.")
            else:
                raise BufferError("Aborted creation of instance with the same name or surname.")
        else:
            raise TypeError("Invalid type of data was entered.")

    def highest_average(self):
        func = operator.attrgetter("average")
        self.group.sort(reverse=True, key=func)
        string = ""
        for i in range(min(5, len(self.group))):
            string += f"{i + 1}. {self.group[i].average} "
        return string


def main():
    tv01 = Group(Student("Denys", "Berezniuk", 1234, 5, 5, 5, 5))
    tv01.add_student(Student("Max", "Nicholiuk", 1233, 4, 4, 4, 4))
    tv01.add_student(Student("Dmytro", "Demianyk", 1235, 5, 4, 5, 4))
    print(tv01.highest_average())
    try:
        tv01.add_student(Student("Dmytro", "No", 1235, 5, 4, 5, 4))
    except BufferError as e:
        print(e)
    try:
        tv01.add_student(Student("No", "Nicholiuk", 1233, 4, 4, 4, 4))
    except BufferError as e:
        print(e)


main()
