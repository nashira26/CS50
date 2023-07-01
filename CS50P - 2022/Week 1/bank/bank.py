
text = input("Greeting: ").strip().lower()
if text[:5] == "hello":
    print("$0")
elif text[0] == "h":
    print("$20")
else:
    print("$100")