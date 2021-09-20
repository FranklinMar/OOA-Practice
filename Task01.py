import sys
import operator


def check(character):
    return character == '+' or character == '-' or character == '*' or character == '/'


if len(sys.argv) > 3 and sys.argv[1].isdigit() and sys.argv[3].isdigit() and check(sys.argv[2]):
    if sys.argv[2] != '/' or int(sys.argv[3]):
        operation = {'*': operator.mul, '/':  operator.truediv, '+': operator.add, '-': operator.sub}
        print(operation[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
    else:
        print("Division by zero.\nNone")
else:
    print(None)
