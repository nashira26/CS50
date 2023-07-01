import csv
import sys

def out(outfile):
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            last, first = row['name'].split(", ")
            house = row['house']
            writer.writerow({"first": first, "last": last, "house": house })
    infile.close()

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (sys.argv[1][-3:] != "csv") or (sys.argv[2][-3:] != "csv"):
    sys.exit("Not a CSV file")
else:
    while True:
        try:
            with open(sys.argv[2], "w") as outfile:
                out(outfile)
                outfile.close()
                sys.exit(0)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")