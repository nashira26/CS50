import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            rand = random.randint(1, level)
            break
        else:
            continue
    except (TypeError, ValueError):
        continue

while True:
    try:
        guess = int((input("Guess: ")))
        if guess < rand:
            print("Too small!")
            continue
        elif guess > rand:
            print("Too large!")
            continue
        else:
            sys.exit("Just right!")
    except (TypeError, ValueError):
        continue

