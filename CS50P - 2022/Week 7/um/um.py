import re
import sys
def main():
    print(count(input("Text: ")))

def count(s):
    count = 0
    if matches := re.findall(r"\bum\b", s.lower()):
        count += len(matches)
    return count

if __name__ == "__main__":
    main()