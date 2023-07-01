import csv
import sys
from tabulate import tabulate

def table(infile):
    table = []
    for row in infile:
        table.append(row)
    return tabulate(table[1:], table[0], tablefmt="grid")

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif (sys.argv[1][-3:] != "csv"):
    sys.exit("Not a CSV file")
else:
    while True:
        try:
            with open(sys.argv[1]) as csvfile:
                reader = csv.reader(csvfile)
                print(table(reader))
                sys.exit(0)
        except FileNotFoundError:
            sys.exit("File does not exist")