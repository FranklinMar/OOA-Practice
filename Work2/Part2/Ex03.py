import statistics
import operator


class Student:
    """
    Instance of class contains data about the student:
    full name, number of grade certificate, a list of grades and average grade.
    """
    def __init__(self, name, surname, number, *args):
        ind = False
        for i in args:
            if not isinstance(i, int):
                ind = True
                break
        if not (isinstance(name, str) and isinstance(surname, str) and isinstance(number, int)) or ind:
            raise TypeError("Invalid type of data was entered.")
        self.name, self.surname, self.number, self.grades = name, surname, number, args
        self.average = statistics.mean(self.grades)


class Group:
    """
    Instance of Class contains a list 'group' of Student class instances, a list
    of names and surnames. Method 'add_student' adds instance of Student class to the
    end of 'group' list, but only if there is no one with the same name or surname.
    This method also forbids adding more than 20 Student instances to the 'group'.
    Method 'highest_average' sorts 'group' list by 'average' in decreasing order and
    returns string with 5 or lower highest average grades.
    """
    group = []
    surnames = []
    names = []

    def __init__(self, student):
        self.group.append(student)
        self.surnames.append(student.surname)
        self.names.append(student.name)

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Invalid type of data was entered.")
        if len(self.group) == 20:
            raise BufferError("Limit of students in a group reached(20).Abort creating instances.")
        if student.surname in self.surnames or student.name in self.names:
            raise BufferError("Aborted creation of instance with the same name or surname.")
        self.group.append(student)
        self.surnames.append(student.surname)
        self.names.append(student.name)

    def highest_average(self):
        self.group.sort(reverse=True, key=operator.attrgetter("average"))
        string = "".join(f"{i + 1}. {self.group[i].average} " for i in range(min(5, len(self.group))))
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
