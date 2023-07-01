def main():
    time = input("What time is it? ")
    t = convert(time)

    if t >= 7.00 and t <= 8.00:
        print("breakfast time")
    elif t >= 12.00 and t <= 13.00:
        print("lunch time")
    elif t >= 18.00 and t <= 19.00:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60
if __name__ == "__main__":
    main()