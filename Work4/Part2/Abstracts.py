from abc import ABC, abstractmethod


# JSON or Database
class ICourse(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, value): pass

    @property
    @abstractmethod
    def teacher(self): pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value): pass

    @property
    @abstractmethod
    def program(self): pass

    @program.setter
    @abstractmethod
    def program(self, value): pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, value): pass

    @property
    @abstractmethod
    def courses(self): pass

    @courses.setter
    @abstractmethod
    def courses(self, value): pass


class ILocalCourse(ICourse, ABC):
    @property
    @abstractmethod
    def address(self): pass

    @address.setter
    @abstractmethod
    def address(self, value): pass


class IOffsiteCourse(ICourse, ABC):
    @property
    @abstractmethod
    def town(self): pass

    @town.setter
    @abstractmethod
    def town(self, value): pass
    # pass


class ICourseFactory(ABC):
    @classmethod
    @abstractmethod
    def teacher_create(cls, name, *courses): pass

    @classmethod
    @abstractmethod
    def course_create(cls, name, teacher, location, course_type="Local", *program): pass

    @classmethod
    @abstractmethod
    def teacher_load(cls): pass

    @classmethod
    @abstractmethod
    def course_load(cls): pass
    
