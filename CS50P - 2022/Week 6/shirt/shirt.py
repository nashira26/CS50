import sys
from PIL import Image, ImageOps

lst = ["csv", "jpg", "jpeg"]
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (((sys.argv[1]).split(".")[1] in lst) or ((sys.argv[2]).split(".")[1] in lst)):
    sys.exit("Invalid output")
elif (sys.argv[1]).split(".")[1] != (sys.argv[2]).split(".")[1]:
    sys.exit("Input and output have different extensions")
else:
    while True:
        try:
            imagefile = Image.open(sys.argv[1])
            break
        except FileNotFoundError:
            sys.exit("Input does not exist")
#open shirt image
shirtfile = Image.open("shirt.png")
#get shirt size
size = shirtfile.size
#fit final image to shirt file size
final_img = ImageOps.fit(imagefile, size)
#paste shirt to muppet
final_img.paste(shirtfile, shirtfile)
#save final image
final_img.save(sys.argv[2])
sys.exit(0)