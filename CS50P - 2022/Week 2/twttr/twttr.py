vowels = "aeiou"
text = input("Input: ")
print("Output: ", end="")
for t in text:
    if t.lower() in vowels:
        continue
    else:
        print(t, end="")
print()