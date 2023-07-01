from validator_collection import validators

def main():
    id = input("What's your email address? ")
    print(validate(id))

def validate(id):
    try:
        ad = validators.email(id)
    except ValueError:
        return "Invalid"
    else:
        return "Valid"

if __name__ == "__main__":
    main()