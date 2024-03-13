def is_float(strings):
    if(strings[0] == "-"):
        strings = strings[1:]
    if strings.replace(".", "").isnumeric():
        return True
    else:
        return False

a = input()
print(is_float(a))