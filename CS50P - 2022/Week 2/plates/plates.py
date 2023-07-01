def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not(s[:2].isalpha()):
        return False
    elif firstnum_zero(s):
        return False
    elif mark(s):
        return False
    elif mid_num(s):
        return False
    else:
        return True


def firstnum_zero(s):
    for i in s:
        if i.isdigit() and i == "0":
            return True
            break
        elif i.isdigit():
            return False
            break
        else:
            pass

def mark(s):
    for i in s:
        if i in [" ", ".", "_"]:
            return True

def mid_num(s):
    i = 0
    while (i < len(s)):
        if (s[i].isdigit()) and not(s[i:].isnumeric()):
            return True
            break
        elif s[i].isdigit() and s[i:].isnumeric():
            return False
            break
        else:
            i += 1
            pass
    return False

main()