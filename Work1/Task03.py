characters = input("Please, enter the formula: ")


def formula(string):
    if string.isdigit():
        return 1
    elif ((string[0] == '+' or string[0] == '-') and string[1:] and string[1].isdigit()) or string[0].isdigit():
        return formula(string[1:len(string)])
    return 0


if formula(characters):
    print(f"True, {eval(characters)}.")
else:
    print("False, None.")
