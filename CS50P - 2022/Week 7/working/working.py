import re
import sys
def main():

    print(convert(input("Hours: ")))
def convert(s):
    try:
        matches = re.search(r"^(\d{1,2})( |:\d{2} )(AM|PM) to (\d{1,2})( |:\d{2} )(AM|PM)$", s)
        hour1, min1, time1, hour2, min2, time2 = matches.group(1), matches.group(2), matches.group(3), matches.group(4),matches.group(5),matches.group(6)
        if hour1[0] == "0" or hour2[0] == "0":
            raise ValueError
        if min1 == " ":
            min1 = 0
        else:
            min1 = int(min1[1:3])
        if min2 == " ":
            min2 = 0
        else:
            min2 = int(min2[1:3])

        if (1 <= int(hour1) <= 12) and (1 <= int(hour2) <= 12) and (0 <= min1 <= 59) and (0 <= min2 <= 59):
            match time1:
                case "AM":
                    xhr1 = int(hour1) % 12
                case "PM" :
                    xhr1 = (int(hour1) % 12) + 12
            match time2:
                case "AM":
                    xhr2 = int(hour2) % 12
                case "PM" :
                    xhr2 = (int(hour2) % 12) + 12
            return f"{xhr1:02}:{min1:02} to {xhr2:02}:{min2:02}"
        else:
            raise ValueError
    except:
        raise ValueError

if __name__ == "__main__":
    main()