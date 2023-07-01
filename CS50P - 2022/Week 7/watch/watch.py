import re
import sys
def main():
    print(parse(input("HTML: ")))

def parse(s):
    #search for iframe
    if re.search(r"<iframe(.)*><\/iframe>",s):
    #if search for matches
        if matches := re.search(r"(https://|http://)(www\.)?youtube\.com/embed/(\w+)\"", s):
        #save the last part
            last = matches.group(3)
        #add last part to the link format
            src = "https://youtu.be/" + last
        #return format
            return src
    #else return none
    else:
        return None

...


if __name__ == "__main__":
    main()