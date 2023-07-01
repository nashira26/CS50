import sys

def count_line(infile):
    count = 0
    for line in infile:
        l = line.lstrip()
        if (l == "") or (l[0].startswith('#')):
            pass
        else:
            count +=1
    return count

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif (sys.argv[1][-2:] != "py"):
    sys.exit("Not a Python file")
else:
    while True:
        try:
            infile = open(sys.argv[1], "r")
            c = count_line(infile)
            print(f"{c}")
            sys.exit(0)
        except FileNotFoundError:
            sys.exit("File does not exist")

