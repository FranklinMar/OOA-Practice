class Rational:
    def __init__(self, num=1, den=1):
        if isinstance(num, int) and isinstance(den, int):
            if den != 0:
                self.__numerator, self.__denominator = num, den
                if self.__denominator < 0:
                    self.__numerator = -self.__numerator
                    self.__denominator = -self.__denominator

                gcd = 1
                num = max(self.__numerator if self.__numerator > 0 else -self.__numerator, self.__denominator)
                for i in range(1, num):
                    if self.__numerator % i == 0 and self.__denominator % i == 0:
                        gcd = i

                self.__numerator /= gcd
                self.__denominator /= gcd
            else:
                print("Error. Division on zero.\nDenominator set to 1 by default.")
                self.__denominator = 1
        else:
            print("Error. Invalid input: Integers required. Setting to 1 by default")
            den = 1 if not isinstance(den, int) else den
            num = 1 if not isinstance(num, int) else num
            self.__numerator, self.__denominator = num, den

    def print_form(self):
        print(f"{self.__numerator}/{self.__denominator}", end="")

    def print_float(self):
        print(self.__numerator / self.__denominator, end="")


def main():
    ration = Rational(2, 4)
    ration.print_float()
    print("\n")
    ration.print_form()
    print("\n")

main()
