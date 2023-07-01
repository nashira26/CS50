lst = dict()
while True:
    try:
        item = input()
        if item in lst:
            lst[item] += 1
        else:
            lst[item] = 1
    except EOFError:
        print("\n")
        break

s_lst = dict(sorted(lst.items()))
for key in s_lst:
    print(f"{s_lst[key]} {key.upper()}")