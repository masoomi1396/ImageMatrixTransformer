from Matrix import *
from PIL import Image
import math

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


def scalingImage(image, factor):
    width, height = image.size
    newWidth, newHeight = int(width * factor), int(height * factor)
    R,G,B = imageMatrixConversion(image)
    newR = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newG = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newB = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    for y in range(newHeight):
        y_old = y * ( (height - 1) / (newHeight - 1) )
        y1 = math.floor(y_old)
        y2 = min(y1 + 1, height - 1)
        dY = y_old - y1
        for x in range(newWidth):
            x_old = x * ( (width - 1) / (newWidth - 1) )
            x1 = math.floor(x_old)
            x2 = min(x1 + 1, width - 1)
            dX = x_old - x1
            
            red_00, red_01, red_10, red_11 = R[y1][x1], R[y1][x2], R[y2][x1], R[y2][x2]
            green_00, green_01, green_10, green_11 = G[y1][x1], G[y1][x2], G[y2][x1], G[y2][x2]
            blue_00,blue_01,blue_10,blue_11 = B[y1][x1], B[y1][x2], B[y2][x1], B[y2][x2]
            
            w_00 = (1 - dX) * (1 - dY)
            w_01 = (dX) * (1 - dY)
            w_10 = (1 - dX) * (dY)
            w_11 = (dX) * (dY)
            
            red = ( red_00 * w_00 + red_01 * w_01 + red_10 * w_10 + red_11 * w_11 )
            green = ( green_00 * w_00 + green_01 * w_01 + green_10 * w_10 + green_11 * w_11 )
            blue = (blue_00 * w_00 + blue_01 * w_01 + blue_10 * w_10 + blue_11 * w_11)
            
            newR[y][x],newG[y][x],newB[y][x] = int(min(255,max(red,0))),int(min(255,max(green,0))),int(min(255,max(blue,0)))
            
    newImage = matrixImageConversion(newR, newG, newB)
    newImage.show()
            

      
            
    
img = Image.open("Test.png")

scalingImage(img, 3)
