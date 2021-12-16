from Abstracts import ITeacher, ILocalCourse, IOffsiteCourse, ICourse, ICourseFactory
from json import load
from os import stat


class Teacher(ITeacher):
    def __init__(self, name, *courses):
        self.name = name
        self.courses = list(*courses)

    def __str__(self):
        return f"Teacher: {self.name}\nCourses:" + \
               ("".join("\n- " + i for i in self.courses) if len(self.courses) else "-")
        # return f"Teacher: {self.name}\nCourses:" + \
        #        ("".join(("\n- Local" if isinstance(i, ILocalCourse) else "\n- Offsite") +
        #                 " Course: " + i for i in self.courses) if len(self.courses) else "-")  # \n\tFull name
        # " Course: " + i.name for i in self.courses

    def assign_to(self, course):
        if not isinstance(course, ICourse):
            raise TypeError(f'unsupported type(s) of {type(course).__name__}')
        # self.courses.append(course)
        self.courses.append(course.name)
        # course.teacher = self
        course.teacher = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'unsupported type(s) for \'name\' of {type(name).__name__}')
        if not all(i.isalpha() or i.isspace() for i in name):
            raise ValueError(f'unsupported value(s) of {name}')
        self.__name = name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        if not isinstance(courses, list):
            raise TypeError(f'unsupported type(s) for \'composition\' of {type(courses).__name__}')
        if len(courses) > 0 and not all(isinstance(i, ICourse) for i in courses):
            raise ValueError(f'unsupported value(s) of {type(courses).__name__}')
        # self.__courses = courses
        self.__courses = [i.name for i in courses]


class LocalCourse(ILocalCourse):
    def __init__(self, name, teacher, local_address, *program):
        self.name = name
        self.teacher = teacher
        self.address = local_address
        self.program = list(*program)

    def __str__(self):  # self.teacher.name if self.teacher else 'None'
        return f"Local course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\t" \
               f"Lab address: {self.address}\n\tCourse topics: " + \
               ("".join("\n" + i for i in self.program) if len(self.program) else 'None')

    def assign_to(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError(f'unsupported type(s) of {type(teacher).__name__}')
        # teacher.courses.append(self)
        teacher.courses.append(self.name)
        # self.teacher = teacher
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'unsupported type(s) for \'name\' of {type(name).__name__}')
        if not all(i.isalnum() or i.isspace() for i in name):
            raise ValueError(f'unsupported value(s) of {name}')
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, ITeacher) and teacher:
            raise TypeError(f'unsupported type(s) for \'teacher\' of {type(teacher).__name__}')
        # self.__teacher = teacher
        self.__teacher = teacher.name if teacher else teacher

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError(f'unsupported type(s) for \'address\' of {type(address).__name__}')
        if not all(i.isascii() for i in address):
            raise ValueError(f'unsupported value(s) of {address}')
        self.__address = address

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not isinstance(program, list):
            raise TypeError(f'unsupported type(s) for \'program\' of {type(program).__name__}')
        if len(program) > 0 and not all(isinstance(i, str) for i in program):
            raise ValueError(f'unsupported value(s) of {type(program).__name__}')
        self.__program = program


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, teacher, town, *program):
        self.name = name
        self.teacher = teacher
        self.town = town
        self.program = list(*program)
        # pass

    def __str__(self):  # self.teacher.name if self.teacher else 'None'
        return f"Local course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\t" \
               f"Town: {self.town}\n\tCourse topics: " + \
               ("".join("\n" + i for i in self.program) if len(self.program) else 'None')

    def assign_to(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError(f'unsupported type(s) of {type(teacher).__name__}')
        # teacher.courses.append(self)
        teacher.courses.append(self.name)
        # self.teacher = teacher
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'unsupported type(s) for \'name\' of {type(name).__name__}')
        if not all(i.isalnum() or i.isspace() for i in name):
            raise ValueError(f'unsupported value(s) of {name}')
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, ITeacher) and teacher:
            raise TypeError(f'unsupported type(s) for \'teacher\' of {type(teacher).__name__}')
        # self.__teacher = teacher
        self.__teacher = teacher.name if teacher else teacher

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, town):
        if not isinstance(town, str):
            raise TypeError(f'unsupported type(s) for \'town\' of {type(town).__name__}')
        if not all(i.isalnum() or i.isspace() or i == '-' for i in town):
            raise ValueError(f'unsupported value(s) of {town}')
        self.__town = town

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not isinstance(program, list):
            raise TypeError(f'unsupported type(s) for \'program\' of {type(program).__name__}')
        if len(program) > 0 and not all(isinstance(i, str) for i in program):
            raise ValueError(f'unsupported value(s) of {type(program).__name__}')
        self.__program = program


class CourseFactory(ICourseFactory):
    pathTeacher = "D:\\Програми\\PyCharm Community Edition 2021.2.1\\PROJECTS\\TestProject\\Work4\\Part2\\teachers.json"
    pathCourses = "D:\\Програми\\PyCharm Community Edition 2021.2.1\\PROJECTS\\TestProject\\Work4\\Part2\\courses.json"

    load_teachers = []
    load_courses = []

    courses = {
        "Local": LocalCourse,
        "Offsite": OffsiteCourse
    }

    @classmethod
    def teacher_create(cls, name, *courses):
        return Teacher(name, *courses)

    @classmethod
    def course_create(cls, name, teacher, location, course_type="Local", *program):
        if not isinstance(course_type, str):
            raise NotImplemented
        if course_type not in cls.courses.keys():
            raise ValueError(f"unsupported value(s) of {course_type}")
        return cls.courses[course_type](name, teacher, location, *program)

    @classmethod
    def course_teacher_load(cls, path_courses, path_teachers):
        if stat(path_courses).st_size <= 2 or stat(path_teachers).st_size <= 2:
            return None
        load_teachers = load(open(path_teachers, 'r'))
        load_courses = load(open(path_courses, 'r'))
        list_teachers = [Teacher(*i.values()) for i in load_teachers]
        list_courses = [LocalCourse(*i.values())
                        if any("Local" in j for j in i.values()) else OffsiteCourse(*i.values())
                        for i in load_courses]

        # list_local = [i if "Local" in i else None for i in list_courses]
        # list_offsite = [i if "Offsite" in i else None for i in list_courses]

        if not len(list_teachers) and not len(list_courses):
            return None
            # raise MemoryError()
        average = None
        for i in [j if j.teacher else None for j in list_courses]:
            average = sum(len(j.courses) for j in list_teachers) / len(list_teachers)
            iterator = iter(list_teachers)
            item = None
            while True:
                try:
                    item = next(iterator)
                    if len(item.courses) < average:
                        break
                except StopIteration:
                    item = None
                    break
            if item:
                i.teacher = item.name
                item.courses.append(i.name)
            else:
                i.teacher = list_teachers[0].name
                list_teachers[0].courses.append(i.name)

        cls.load_teachers.extend(list_teachers)
        cls.load_courses.extend(list_courses)
        # for i in range(len(list_courses)):
        #     item = list_courses[i]
        #
        #     i.assign_to()

    @classmethod
    def teacher_load(cls):
        iterator = iter(cls.load_teachers)
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                break

    @classmethod
    def course_load(cls):
        iterator = iter(cls.load_courses)
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                break


test = Teacher("Nataliya")
testCourse = LocalCourse("Python", None, "HQ Lab1")
testoffsite = OffsiteCourse("Python", None, "HQ Lab1")
print(test)
print(testCourse)
print(test.__dict__)
print(testCourse.__dict__)
print(testoffsite.__dict__)
test.assign_to(testCourse)
print(test)
print(testCourse)
