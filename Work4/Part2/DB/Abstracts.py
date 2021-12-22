from abc import ABC, abstractmethod


class ICourse(ABC):
    """Course abstract class"""
    @property
    @abstractmethod
    def name(self):
        """'name' attribute getter"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """'name' attribute setter"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """'teacher' attribute getter"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """'teacher' attribute setter"""
        pass

    @property
    @abstractmethod
    def program(self):
        """'program' attribute getter"""
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        """'program' attribute setter"""
        pass


class ITeacher(ABC):
    """Teacher abstract class"""
    @property
    @abstractmethod
    def name(self):
        """'name' attribute getter"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """'name' attribute setter"""
        pass

    @property
    @abstractmethod
    def courses(self):
        """'courses' attribute getter"""
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        """'courses' attribute setter"""
        pass


class ILocalCourse(ICourse, ABC):
    """Local Course abstract class"""
    @property
    @abstractmethod
    def address(self):
        """'address' attribute getter"""
        pass

    @address.setter
    @abstractmethod
    def address(self, value):
        """'address' attribute setter"""
        pass


class IOffsiteCourse(ICourse, ABC):
    """Offsite Course abstract class"""
    @property
    @abstractmethod
    def town(self):
        """'town' attribute setter"""
        pass

    @town.setter
    @abstractmethod
    def town(self, value):
        """'town' attribute setter"""
        pass


class ICourseFactory(ABC):
    """Course Factory abstract class"""
    @classmethod
    @abstractmethod
    def teacher_create(cls, name, *courses):
        """Factory method for creating teacher"""
        pass

    @classmethod
    @abstractmethod
    def course_create(cls, name, teacher, location, course_type="Local", *program):
        """Factory method for creating course
        Types of courses: Local/Offsite"""
        pass

    @classmethod
    @abstractmethod
    def teacher_get(cls):
        """Factory generator method for getting teachers from queue"""
        pass

    @classmethod
    @abstractmethod
    def course_get(cls):
        """Factory generator method for getting courses from queue"""
        pass
