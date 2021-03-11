from PIL import Image
import os

# Get Terminal size
rows, columns = os.popen('stty size', 'r').read().split()
im = Image.open("assets/5733121373_044ed8cb27_o.jpg")
# Convert image to grayscale
im = im.convert('L')
im = im.transpose(Image.ROTATE_90)
width, height = im.size
im = im.resize((int(width/4), int(height/4)), Image.ANTIALIAS)
# im = im.resize((int(rows), int(columns)), Image.ANTIALIAS)
width, height = im.size
# im.show()
f = open("ascii_image.txt", "w+")
max = max(list(im.getdata()))
grayscale = "@%#*+=-:."
dyn_range = len(grayscale)

for w in range(width):
    f.write("\n")
    for h in range(height):
        gray = im.getpixel((w,h))
        gray_index = ((1 / max) * gray) * dyn_range -1
#         print(grayscale[int(gray_index)], end='')
        f.write(grayscale[int(gray_index)])

        