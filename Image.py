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
            

def findingBoundryOfRotation(width,height,angle,point):
    sinAngle = math.sin(angle)
    cosAngle = math.cos(angle)
    
    x1 = 0
    x2 = width - 1
    y1 = 0
    y2 = height - 1
    
    xNew = []
    yNew = []
    corners = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
    
    for corner in corners:
        x = corner[0]
        y = corner[1]
        xShifted = x - point[0]
        yShifted = y - point[1]
        xRot =  xShifted * cosAngle - yShifted * sinAngle
        yRot =  xShifted * sinAngle + yShifted * cosAngle
        xNew.append(xRot + point[0]) 
        yNew.append(yRot + point[1]) 
    xNew.sort()
    yNew.sort()
    
    newWidth = xNew[3] - xNew[0] 
    newHeight = yNew[3] - yNew[0]
    
    offsetX = -xNew[0]
    offsetY = -yNew[0]
    
    return math.ceil(newWidth), math.ceil(newHeight), offsetX, offsetY
    
    pass


def rotatedImage(image, angle, point=(0,0)):
    angle *= math.pi / 180
    width, height = image.size
    rotationX = point[0]
    rotationY = point[1]
    sinAngle = math.sin(angle)
    cosAngle = math.cos(angle)
    R,G,B = imageMatrixConversion(image)
    
    newWidth, newHeight, offsetX, offsetY = findingBoundryOfRotation(width, height, angle, point)
    
    
    newR = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newG = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newB = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    
    
    for y in range(newHeight):
        yShifted = y - offsetY
        yCentered = yShifted - rotationY
        for x in range(newWidth):
            xShifted = x - offsetX
            xCentered = xShifted - rotationX
            
            x_old = xCentered * cosAngle + yCentered * sinAngle
            y_old = (-xCentered) * sinAngle + yCentered * cosAngle
            
            x_src = x_old + rotationX
            y_src = y_old + rotationY
            
            
            if x_src < 0 or x_src >= width or y_src < 0 or y_src >= height:
                newR[y][x],newG[y][x],newB[y][x] = 0,0,0
                continue
            
            y1 = math.floor(y_src)
            y2 = min(y1 + 1, height - 1)
            dY = y_src - y1
            
            x1 = math.floor(x_src)
            x2 = min(x1 + 1, width - 1)
            dX = x_src - x1
            
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

    
def grayScaleFunctino(image):
    width, height = image.size

    R,G,B = imageMatrixConversion(image)
    newR = [[0 for _ in range(width)] for _ in range(height)]
    newG = [[0 for _ in range(width)] for _ in range(height)]
    newB = [[0 for _ in range(width)] for _ in range(height)]
    gray = 0
    for y in range(height):
        for x in range(width):
            gray =  min(255, int(R[y][x] * 0.299 +  G[y][x] * 0.578 +  B[y][x] * 0.114))
            gray = max(0, gray)
            
            newR[y][x] = gray
            newG[y][x] = gray
            newB[y][x] = gray
    newImage = matrixImageConversion(newR, newG, newB)
    newImage.show()


def findingBoundryOfSkew(width, height, skewMatrix):
    x1 = 0
    y1 = 0
    x2 = width - 1
    y2 = height - 1
    xNew = []
    yNew = []
    corners = [(x1,y1),(x1,y2), (x2,y1), (x2,y2)]
    
    for corner in corners:
        point = [[corner[0]], [corner[1]]]
        newPoint = matrixMultiplication(skewMatrix, point)
        xNew.append(newPoint[0][0])
        yNew.append(newPoint[1][0])
    xNew.sort()
    yNew.sort()
    
    
    newWidth = xNew[3] - xNew[0] 
    newHeight = yNew[3] - yNew[0] 
    
    
    return math.ceil(newWidth), math.ceil(newHeight)


def skewImage(image, skewFactor, type="h"):
    if type.lower() == 'h':
        skewMatrix = [[1,skewFactor],[0,1]]
        inverseSkewMatrix = [[1,-skewFactor],[0,1]]
    else:
        skewMatrix = [[1,0],[skewFactor,1]]
        inverseSkewMatrix = [[1,0],[-skewFactor,1]]
    width, height = image.size
    newWidth,newHeight = findingBoundryOfSkew(width, height, skewMatrix)
    R,G,B = imageMatrixConversion(image)
    newR = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newG = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    newB = [[0 for _ in range(newWidth)] for _ in range(newHeight)]
    for y in range(newHeight):
        for x in range(newWidth):
            point = [[x],[y]]
            oldPoint = matrixMultiplication(inverseSkewMatrix, point)
            x_src = oldPoint[0][0]
            y_src = oldPoint[1][0]
            if x_src < 0 or x_src >= width or y_src < 0 or y_src >= height:
                newR[y][x],newG[y][x],newB[y][x] = 0,0,0
                continue
            
            y1 = math.floor(y_src)
            y2 = min(y1 + 1, height - 1)
            dY = y_src - y1
            
            x1 = math.floor(x_src)
            x2 = min(x1 + 1, width - 1)
            dX = x_src - x1
            
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

width,height = img.size

skewImage(img, 0.3, 'v')
