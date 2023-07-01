import inflect

p = inflect.engine()

lst = []
while True:
    try:
        name = input("Name: ")
        lst.append(name)
    except EOFError:
        print()
        break

names = p.join(lst)
print("Adieu, adieu, to " + names)
