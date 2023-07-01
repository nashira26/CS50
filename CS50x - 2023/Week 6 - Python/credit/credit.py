while True:
    try:
        num = int(input("Number: "))
    except ValueError:
        pass
    else:
        break

def type_of(num):
    n = str(num)
    if len(n) == 15 and (n[:2] == "34" or n[:2] == "37"):
        return "AMEX"
    elif len(n) == 16 and (int(n[:2]) > 50 and int(n[:2]) < 56):
        return "MASTERCARD"
    elif (len(n) > 12 and len(n) < 17) and (n[0] == "4"):
        return "VISA"
    else:
        return "INVALID"

def valid(num):
    n = str(num)
    l = len(n)
    sum = 0
    for i in range(-2, -(l+1), -2):
        product = int(n[i]) * 2
        if product > 9:
            sum += (1 + (product % 10))
        else:
            sum += product

    for i in range(-1, -(l+1), -2):
        sum += int(n[i])

    if (str(sum))[-1] == "0":
        return True
    else:
        return False

if type_of(num) == "INVALID":
    print("INVALID")
elif not valid(num):
    print("INVALID")
else:
    print(f"{type_of(num)}")
