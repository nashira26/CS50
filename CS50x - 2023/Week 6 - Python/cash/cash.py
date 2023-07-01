while True:
    try:
        c = float(input("Owed: "))
        if c < 0.00:
            raise ValueError
            pass
    except ValueError:
        pass
    else:
        count = 0
        c = c * 100
        break

if c >= 25:
    i = int(c / 25)
    count += i
    c -= (i * 25)
if c >= 10:
    i = int(c / 10)
    count += i
    c -= (i * 10)
if c >= 5:
    i = int(c / 5)
    count += i
    c -= (i * 5)
if c >= 1:
    count += c
print(int(count))
