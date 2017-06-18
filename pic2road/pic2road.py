from PIL import Image

imagepaths = input("Image Path?")
im = Image.open(imagepaths)
pix = im.load()

width, height = im.size()

for x in range(width):
    for y in range(height):
        r, g, b = pix(x, y)
        if r < 125 and b < 125 and g < 125:
            print(x, y)
