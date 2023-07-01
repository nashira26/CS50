def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
         count += 1
    return count

def count_words(text):
    count = 1
    for i in range(len(text)):
        if (text[i] == " "):
           count += 1
    return count

def count_sentences(text):
    count = 0
    for i in range(len(text)):
        if text[i] in [".", "!", "?"]:
            count += 1
    return count

txt = input("Text: ")
L = float((count_letters(txt) / count_words(txt)) * 100)
S = float((count_sentences(txt) / count_words(txt)) * 100)

grade = round((0.0588 * L) - (0.296 * S) - 15.8)
if (grade >= 16):
    print("Grade 16+")
elif (grade < 1):
    print("Before Grade 1")
else:
    print(f"Grade {grade}")


