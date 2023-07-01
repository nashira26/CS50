import csv
import sys


def main():

    #Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    #Read database file into a variable
    with open(sys.argv[1], 'r') as csvfile:
        d_reader = csv.DictReader(csvfile)
        headers = d_reader.fieldnames
        data = [x for x in d_reader]
    subs = headers[1:]

    #Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as seqfile:
        sequence = seqfile.read().replace("\n","")

    #Find longest match of each STR in DNA sequence
    matches_dict = {}
    for sub in subs:
        matches_dict[sub] = str(longest_match(sequence, sub))
    result = "No match"
    #Check database for matching profiles
    for d in data:
        matches = 0
        for m in matches_dict:
            if d[m] == matches_dict[m]:
                matches += 1
        if matches == len(matches_dict):
            result = d["name"]
            break
    print(result)




def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
