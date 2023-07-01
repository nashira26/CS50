import random


def main():
    n = int(get_level())
    count = 0
    score = 0
    while count < 10:
        x = int(generate_integer(n))
        y = int(generate_integer(n))
        times = 0
        while times < 3:
            ans = input(f"{x} + {y} = ")
            if ans == str(x + y):
                count += 1
                break
            else:
                times += 1
                print("EEE")
                continue

        if times == 3:
            print(f"{x} + {y} = {x+y}")
            count += 1
        else:
            score += 1

    print("Score: ", score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                return n
        except (TypeError, ValueError):
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()