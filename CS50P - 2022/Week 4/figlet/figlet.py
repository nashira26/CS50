from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
lst = figlet.getFonts()

if (len(sys.argv) == 1):
    f = choice(lst)
elif (len(sys.argv) == 3) and ((sys.argv[1] == "-f") or (sys.argv[1] == "--font")) and (sys.argv[2] in lst):
    f = sys.argv[2]
else:
    sys.exit("Invalid Usage")

s = input("Input: ")
figlet.setFont(font=f)
print("Output:\n")
print(figlet.renderText(s))