import sys
import operator


def check(character):
    return character == 'add' or character == 'sub' or character == 'mul' or character == 'div'


if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit() and check(sys.argv[1]):
        if sys.argv[1] != 'div' or int(sys.argv[3]):
        operation = {'mul': operator.mul, 'div': operator.truediv, 'add': operator.add, 'sub': operator.sub}
        print(operation[sys.argv[1]](int(sys.argv[2]), int(sys.argv[3])))
    else:
        print("Division by zero.\nNone")
else:
    print(None)
