import math


class Rational:
    """
    Attributes:
    'numerator' and 'denominator'.
    Contains overloaded operators
    """
    def __reducing(self):
        num = math.gcd(self.numerator, self.denominator)
        self.numerator //= num
        self.denominator //= num

    def __init__(self, num=1, den=1):
        self.numerator, self.denominator = num, den
        if self.denominator < 0:
            self.numerator, self.denominator = -self.numerator, -self.denominator
        self.__reducing()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def float(self):
        return str(self.numerator / self.denominator)

    # Rational * other
    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator, denominator = self.numerator * other, self.denominator
            return Rational(numerator, denominator)
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational / other
    def __truediv__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            denominator, numerator = self.denominator * other, self.numerator
            return Rational(numerator, denominator)
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational + other
    def __add__(self, other):
        if isinstance(other, Rational):
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator, denominator = self.numerator + other * self.denominator, self.denominator
            return Rational(numerator, denominator)
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational - other
    def __sub__(self, other):
        if isinstance(other, Rational):
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator, denominator = self.numerator - other * self.denominator, self.denominator
            return Rational(numerator, denominator)
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational *= other
    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
            if self.denominator < 0:
                self.numerator, self.denominator = -self.numerator, -self.denominator
            self.__reducing()
        elif isinstance(other, int):
            self.numerator *= other
            self.__reducing()
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational /= other
    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.denominator
            self.denominator *= other.numerator
            if self.denominator < 0:
                self.numerator, self.denominator = -self.numerator, -self.denominator
            self.__reducing()
        elif isinstance(other, int):
            self.denominator *= other
            if self.denominator < 0:
                self.numerator, self.denominator = -self.numerator, -self.denominator
            self.__reducing()
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational += other
    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
            if self.denominator < 0:
                self.numerator, self.denominator = -self.numerator, -self.denominator
            self.__reducing()
        elif isinstance(other, int):
            self.numerator += other * self.denominator
            self.__reducing()
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    # Rational -= other
    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator *= other.denominator
            if self.denominator < 0:
                self.numerator, self.denominator = -self.numerator, -self.denominator
            self.__reducing()
        elif isinstance(other, int):
            self.numerator -= other * self.denominator
            self.__reducing()
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        return (self.numerator, self.denominator) == (other.numerator, other.denominator)
        # return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        # return (self.numerator != other.numerator) or (self.denominator != other.denominator)
        return (self.numerator, self.denominator) != (other.numerator, other.denominator)

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')
        return self.numerator * other.denominator <= other.numerator * self.denominator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, den):
        if not isinstance(den, int):
            raise TypeError("Invalid type of data entered.")
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__denominator = den

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, num):
        if not isinstance(num, int):
            raise TypeError("Invalid type of data entered.")
        self.__numerator = num


test = Rational(1, 2)
test1 = Rational(1, 3)
print(f"1.{test}")
print((test * 4))
print(f"2.{test}")
print((test / 4))
print(f"3.{test}")
print((test + 4))
print(f"4.{test}")
print((test - 4))
print(test != test1)
print(test == test)
print((test * test1))
print((test / test1))
print((test + test1))
print((test - test1))
