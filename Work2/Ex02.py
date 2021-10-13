import math

class Rational:
    def __init__(self, num=1, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Invalid type of data entered.")
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__numerator, self.__denominator = num, den
        if self.__denominator < 0:
            self.__numerator, self.__denominator = -self.__numerator, -self.__denominator
        num = math.gcd(self.__numerator, self.__denominator)
        self.__numerator //= num
        self.__denominator //= num

    def print_form(self):
        return f"{self.__numerator}/{self.__denominator}"

    def print_float(self):
        return str(self.__numerator / self.__denominator)


def main():
    ration = Rational(2, 4)

    print(f"{ration.print_float()}\n{ration.print_form()}\n")
    try:
        ration = Rational("5", "no")
    except TypeError as e:
        print("Invalid types of data entered in class instance\n")
    try:
        ration = Rational(5, 0)
    except ValueError as e:
        print("Division on zero.\n")

        
main()
