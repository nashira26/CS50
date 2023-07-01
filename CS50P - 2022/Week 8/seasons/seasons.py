from datetime import date
import re, sys, operator
import inflect
p = inflect.engine()

def main():
    try:
        dob = validate(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input")
    else:
        d = age(dob)
        print(f'{p.number_to_words(d, andword="").capitalize()} minutes')

def validate(d):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", d):
        try:
            dob = date(int(d.split("-")[0]), int(d.split("-")[1]),int(d.split("-")[2]))
            return dob
        except ValueError:
            raise ValueError
    else:
        raise ValueError

def age(dob):
    date_today = date.today()
    d = operator.sub(date_today, dob)
    return int(d.days) * 24 * 60

if __name__ == "__main__":
    main()