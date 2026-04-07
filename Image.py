from Matrix import *
from PIL import Image

def imageMatrixConversion(image):
    image = image.convert("RGB")
    width, height = image.size
    pixels = image.load()
    R = [[0 for _ in range(width)] for _ in range(height)]
    G = [[0 for _ in range(width)] for _ in range(height)]
    B = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            R[y][x], G[y][x], B[y][x] = pixels[x,y]
            
    return R,G,B


def matrixImageConversion(R,G,B):
    width = len(R[0])
    height = len(R)
    newImage = Image.new("RGB", (width,height))
    pixels = newImage.load()

    for y in range(height):
        for x in range(width):
            pixels[x,y] = (R[y][x],G[y][x],B[y][x])

    return newImage

img = Image.open("Test.png")

R,G,B = imageMatrixConversion(img)

newImage = matrixImageConversion(R, G, B)

newImage.show()