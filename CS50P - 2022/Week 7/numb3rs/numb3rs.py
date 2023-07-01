import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    i = ip.strip()
    if re.search(r"^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*$", i):
        nums = ip.split(".")
        for num in nums:
            if int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()