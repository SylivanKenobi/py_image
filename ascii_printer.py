from PIL import Image
import os

# Get Terminal size
rows, columns = os.popen('stty size', 'r').read().split()
im = Image.open("assets/2021_0226_20372800.jpg")
# Convert image to grayscale
im = im.convert('L')
im = im.transpose(Image.ROTATE_180)
width, height = im.size
im = im.resize((int(width/2), int(height/2)), Image.ANTIALIAS)
width, height = im.size
# im.show()
f = open("ascii_image.txt", "w+")

for w in range(width):
    f.write("\n")
    for h in range(height):
        gray = im.getpixel((w,h))
        # print(gray)
        if (gray < 40):
            f.write("#")
        elif (gray >= 40 and gray < 80):
            f.write("P")
        elif (gray >= 80 and gray < 120):
            f.write("O")
        elif (gray >= 120 and gray < 160): 
            f.write("I")
        elif (gray >= 160 and gray < 200):
            f.write(";")
        elif (gray >= 200 and gray < 240):
            f.write(":")
        else:
            f.write(".")

# for w in range(width):
#     print("")
#     for h in range(height):
#         gray = im.getpixel((w,h))
#         # print(gray)
#         if (gray < 10):
#             print("#", end='')
#         elif (gray >= 20 and gray < 50):
#             print("P", end='')
#         elif (gray >= 50 and gray < 80):
#             print("O", end='')
#         elif (gray >= 80 and gray < 110): 
#             print("I", end='')
#         elif (gray >= 110 and gray < 140):
#             print(";", end='')
#         elif (gray >= 140 and gray < 240):
#             print(":", end='')
#         else:
#             print(".", end='')
        