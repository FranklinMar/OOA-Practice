from Abstracts import ITeacher, ILocalCourse, IOffsiteCourse, ICourse, ICourseFactory
import sqlite3


class Teacher(ITeacher):
    """A class for representing Teachers

    Implements ITeacher abstract class

    Attributes
    name: str
        A string with the name of teacher
    courses: list[str]
        A list with names of courses assigned for teacher"""
    def __init__(self, name, *courses):
        """
        Create instance of teacher
        :param name: A name of teacher
        :param courses: A list of courses for this teacher (Default:None)
        """
        self.name = name
        self.courses = list(*courses)

    def __str__(self):
        """
        Information about instance in human-readable form
        :return: str: Information about teacher
        """
        return f"Teacher: {self.name}\nCourses:" + \
               ("".join("\n- " + i for i in self.courses) if len(self.courses) else "-")

    def assign_to(self, course):
        """
        Assigns instance of teacher to a course
        :param course: Instance of ICourse implementation to assign
        :return: None
        """
        if not isinstance(course, ICourse):
            raise TypeError(f'unsupported type(s) of {type(course).__name__}')
        self.courses.append(course.name)
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
        self.__courses = [i.name for i in courses]


class LocalCourse(ILocalCourse):
    """A class for representing Local Courses

    Implements ICourse abstract class

    Attributes
    name: str
        A string with name of the course
    teacher: str
        A string with name of the teacher of the course
    local_address: str
        An address/No. of lab for course
    program: list[str]
        A list with names of topics of the course. Sequence of topics"""
    def __init__(self, name, teacher, local_address, *program):
        """
        Create instance of local course
        :param name: Name of the course
        :param teacher: Teacher assigned to course
        :param local_address: An address of lab for course
        :param program: A list of topics of the course
        """
        self.name = name
        self.teacher = teacher
        self.address = local_address
        self.program = list(*program)

    def __str__(self):
        """
        Information about instance in human-readable form
        :return: str: Information about Local Course
        """
        return f"Local course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\t" \
               f"Lab address: {self.address}\n\tCourse topics: " + \
               ("".join("\n- " + i for i in self.program) if len(self.program) else 'None')

    def assign_to(self, teacher):
        """
        Assign this course to a teacher
        :param teacher: Instance of ITeacher implementation to assign
        :return: None
        """
        if not isinstance(teacher, ITeacher):
            raise TypeError(f'unsupported type(s) of {type(teacher).__name__}')
        teacher.courses.append(self.name)
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
    """A class for representing Offsite Courses

    Implements IOffsiteCourse abstract class

    Attributes
    name: str
        A string with name of the course
    teacher: str
        A string with name of the teacher of the course
    town: str
        A town of domain for course
    program: list[str]
        A list with names of topics of the course. Sequence of topics"""
    def __init__(self, name, teacher, town, *program):
        """
        Create instance of offsite course
        :param name: Name of the course
        :param teacher: Teacher assigned to course
        :param town: A town of domain for course
        :param program: A list of topics of the course
        """
        self.name = name
        self.teacher = teacher
        self.town = town
        self.program = list(*program)

    def __str__(self):
        """
        Information about instance in human-readable form
        :return: str: Information about Local Course
        """
        return f"Offsite course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\t" \
               f"Town: {self.town}\n\tCourse topics: " + \
               ("".join("\n- " + i for i in self.program) if len(self.program) else 'None')

    def assign_to(self, teacher):
        """
        :param teacher: Instance of ITeacher implementation to assign
        :return: None
        """
        if not isinstance(teacher, ITeacher):
            raise TypeError(f'unsupported type(s) of {type(teacher).__name__}')
        teacher.courses.append(self.name)
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
    """CourseFactory class for creating courses and teachers

    Implements ICourseFactory

    Class Attributes:
    load_teachers : list[Teacher]
        Queue of loaded teachers from external sources
    load_courses : list[LocalCourse | Offsite]
        Queue of loaded teachers from external sources
    courses : dict{str : class}
        Dictionary for type of course
    """

    list_teachers = []
    list_courses = []
    courses = {'local': LocalCourse, 'offsite': OffsiteCourse}

    @classmethod
    def teacher_create(cls, name, *courses):
        return Teacher(name, *courses)

    @classmethod
    def course_create(cls, name, teacher, location, course_type="Local", *program):
        if not isinstance(course_type, str):
            raise NotImplementedError
        if course_type.lower() not in cls.courses.keys():
            raise ValueError(f"unsupported value(s) of {course_type}")
        return cls.courses[course_type.lower()](name, teacher, location, *program)

    @classmethod
    def course_teacher_load(cls, path_to_db):
        """
        Method of creating instances from databases.
        Loading instances to the queues.
        :param path_to_db: Path to the database with courses and teachers
        :return: None
        """
        connection = sqlite3.connect(path_to_db)

        cursor = connection.cursor()
        list_teachers = []
        list_courses = []

        table_courses = cursor.execute('SELECT * FROM Course')  
        for i in [j for j in table_courses]:
            topics = []
            if i[4]:
                topics = cursor.execute(f'SELECT Topic FROM Topics WHERE id = {i[4]}')
                topics = [j for j in topics]
            if i[1]:
                item_teacher = Teacher(*[j for j in
                                       cursor.execute(f'SELECT name FROM Teachers WHERE name = "{i[1]}"')][0])
                list_teachers.append(item_teacher)
                item_course = cls.courses[i[3].lower()](i[0], item_teacher, i[2], *topics)
                list_courses.append(item_course)
                item_teacher.assign_to(item_course)
            else:
                item_course = cls.courses[i[3].lower()](i[0], i[1], i[2], *topics)
                list_courses.append(item_course)

        table_teachers = cursor.execute('SELECT name FROM Teachers WHERE courses IS NULL')
        cls.list_teachers.extend(Teacher(i) for i in table_teachers)
        cls.list_teachers.extend(list_teachers)
        cls.list_courses.extend(list_courses)
        connection.close()

    @classmethod
    def course_form(cls):
        """
        Method of forming courses, using loaded instances, by assigning teachers to courses without a teacher
        :return: bool - if any Teacher was assigned to a Course
        """
        list_iteration = [j if not (j.teacher if j else None) else None for j in cls.list_courses]
        if not len(list_iteration) or not len(cls.list_teachers):  # or not len(cls.list_courses):
            return False
        average = 0
        for i in list_iteration:
            average = sum(len(j.courses) for j in cls.list_teachers) / len(cls.list_teachers)
            iterator = iter(cls.list_teachers)
            item = None
            while True:
                try:
                    item = next(iterator)
                    if len(item.courses) < average:
                        break
                except StopIteration:
                    break
            if item:
                i.assign_to(item)
            else:
                i.assign_to(cls.list_teachers[0])
        return True

    @classmethod
    def teacher_get(cls):
        while True:
            try:
                yield cls.list_teachers.pop(0)
            except IndexError:
                return

    @classmethod
    def course_get(cls):
        while True:
            try:
                yield cls.list_courses.pop(0)
            except IndexError:
                return


if __name__ == "__main__":
    # test = Teacher("Nataliya")
    # testCourse = LocalCourse("Python", None, "HQ Lab1")
    # testoffsite = OffsiteCourse("Python", None, "HQ Lab1")
    # print(test)
    # print(testCourse)
    # print(test.__dict__)
    # print(testCourse.__dict__)
    # print(testoffsite.__dict__)
    # test.assign_to(testCourse)
    # print(test)
    # print(testCourse)
    # print(CourseFactory.course_create("Python", None, "HQ Lab1", 'Offsite'))
    CourseFactory.course_teacher_load(
        "D:\\Програми\\PyCharm Community Edition 2021.2.1\\PROJECTS\\TestProject\\Work4\\Part2\\DB\\Teach.db")
    # CourseFactory.course_form()
    print(next(CourseFactory.course_get()))
    print(next(CourseFactory.teacher_get()))
    print(next(CourseFactory.course_get()))
    print(next(CourseFactory.teacher_get()))
