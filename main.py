from PIL import Image
import sys

# Luminance Symbols 0.0 - 1.0
lum_sym = ['.', '*', '^', '~', '!', '&', '$', '%', '#', '@']
ascii_buf = ""

if len(sys.argv) != 3:
    print("[-] Usage: python main.py <image file> <resize rate>")
    exit(1)

resize_rate = float(sys.argv[2])

img = Image.open(sys.argv[1]).convert("LA") # Open image then convert to grayscale
img = img.rotate(90)
WIDTH, HEIGHT = img.size
WIDTH = int(WIDTH * resize_rate)
HEIGHT = int(HEIGHT * resize_rate)
img.thumbnail((WIDTH, HEIGHT), Image.ANTIALIAS) # Resize Image
pix = img.load() # Image pixels

for x in range(WIDTH):
    for y in range(HEIGHT):
        gscale,_ = pix[x,y]
        gscale = int(round(gscale/255, 1) * 10) - 1
        ascii_buf += lum_sym[gscale]
    ascii_buf += "\n"

print(ascii_buf)