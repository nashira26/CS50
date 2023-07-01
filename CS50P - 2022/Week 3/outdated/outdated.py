
lst= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    d = input("Date: ")
    try:
        x, y, z = d.split("/")
        if int(x) < 13 and int(y) < 32 and int(z) > 0:
            yr = int(z)
            m = int(x)
            d = int(y)
            break
    except:
        try:
            x, y, z = d.split(" ")
            y1 = y.replace(",","")
            if (x in lst) and (int(y1) < 32) and (int(z) > 0) and (y.isnumeric() == False):
                yr = int(z)
                m = int(lst.index(x)) + 1
                d = int(y1)
                break
            else:
                pass
        except (ValueError, TypeError, KeyError):
            pass
    else:
        pass


print(f"{yr}-{m:02}-{d:02}")
