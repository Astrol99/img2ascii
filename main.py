from PIL import Image
import sys

if len(sys.argv) != 2:
    print("[-] Usage: python main.py <image file>")
    exit(1)

imageFile = sys.argv[1]

# Luminance Symbols 0.0 - 1.0
lum_sym = ['.', '*', '^', '~', '!', '&', '$', '%', '#', '@']