def matrixSum (matrix_1 ,matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("There is dimension Error in matrixSum Function")
    matrixOfSum = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_2)):
        for column in range(len(matrix_2[row])):
          matrixOfSum[row][column] = matrix_1[row][column] + matrix_2[row][column]
    return matrixOfSum

          
def matrixSub (matrix_1 ,matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]): 
        raise ValueError("There is a dimension Error in matrixSub Function")
    matrixOfSub = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_2)):
        for column in range(len(matrix_2[row])):
          matrixOfSub[row][column] = matrix_1[row][column] - matrix_2[row][column]
    return matrixOfSub


def matrixScalar (matrix_1, k):
    matrixOfScalar = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_1)):
        for column in range(len(matrix_1[row])):
            matrixOfScalar[row][column] = matrix_1[row][column] * k
    return matrixOfScalar
        

def matrixMultiplication (matrix_1, matrix_2):
    if len(matrix_1[0]) != len(matrix_2) :
        raise ValueError("Number of column 1 is not equal to row of 2")
    matrixOfMulti = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
    for row in range(len(matrixOfMulti)):
        for column in range(len(matrixOfMulti[row])):
            multi_num = 0
            for room in range(len(matrix_1[0])):
                multi_num = multi_num + (matrix_1[row][room] * matrix_2[room][column])
            matrixOfMulti[row][column] = multi_num   
    return matrixOfMulti
            

def matrixTranspose (matrix_1):
    matrixOfTranspose = [[0 for _ in range (len(matrix_1))] for _ in range (len(matrix_1[0]))]
    for row in range(len(matrix_1)):
        for column in range(len(matrix_1[row])):
            matrixOfTranspose[column][row] = matrix_1[row][column]
    return matrixOfTranspose


    
#x = [[1,2,3],[4,5,6],[7,8,9]]
#y = [[1],[2],[3]]





