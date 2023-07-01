while True:
    try:
        h = int(input("Height: "))
        if h < 1 or h > 8:
            raise ValueError
            pass
    except ValueError:
        pass
    else:
        for i in range(1, h+1):
            print(("#" * i).rjust(h, " "), "", ("#" * i))
        break