text = input()
try:
    print(text.lower())
except TypeError:
    print(text)