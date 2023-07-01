def main():
    mass = int(input())
    print(convert(mass))

def convert(mass):
    energy = mass * (300000000**2)
    return energy
main()