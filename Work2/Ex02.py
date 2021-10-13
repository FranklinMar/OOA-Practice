class Rational:
    def __init__(self, num=1, den=1):
        if isinstance(num, int) and isinstance(den, int) and den != 0:
            self.__numerator, self.__denominator = num, den
            if self.__denominator < 0:
                self.__numerator = -self.__numerator
                self.__denominator = -self.__denominator

            gcd = 1
            for i in range(1, max(self.__numerator if self.__numerator > 0 else -self.__numerator, self.__denominator)):
                if self.__numerator % i == 0 and self.__denominator % i == 0:
                    gcd = i

            self.__numerator /= gcd
            self.__denominator /= gcd
        else:
            raise BaseException

    def print_form(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))

    def print_float(self):
        return str(self.__numerator / self.__denominator)


def main():
    ration = Rational(2, 4)

    print(ration.print_float() + "\n" + ration.print_form() + "\n")
    try:
        ration = Rational("5", "no")
    except BaseException:
        print("Invalid types of data entered in class instance\n")
    try:
        ration = Rational(5, 0)
    except BaseException:
        print("Division on zero.\n")


main()
