while True:
    try:
        x, y = input("Fraction: ").split("/")
        fuel = int(x) / int(y)
        if fuel <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
z = round(fuel * 100)
if z <= 1:
    print("E")
elif z >= 99:
    print("F")
else:
    print(f"{z}%")

