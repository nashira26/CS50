name = input("camelCase: ")
print("snake_case: ", end="")
for n in name:
    if n.islower():
        print(n, end="")
    else:
        s = n.lower()
        print("_" + s , end="")
print()