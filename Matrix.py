def matrixSum (matrix_1 ,matrix_2):
    matrixOfSum = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_2)):
        for column in range(len(matrix_2[row])):
          matrixOfSum[row][column] = matrix_1[row][column] + matrix_2[row][column]
    return matrixOfSum
            
def matrixSub (matrix_1 ,matrix_2):
    matrixOfSub = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_2)):
        for column in range(len(matrix_2[row])):
          matrixOfSub[row][column] = matrix_1[row][column] - matrix_2[row][column]
    return matrixOfSub

def matrixScalar (matrix_1, k):
    matrixOfScalar = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_1)):
        for column in range(len(matrix_1[row])):
            matrixOfScalar[row][column] = (matrix_1[row][column] * k)
    return matrixOfScalar

def matrixMultipication (matrix_1, matrix_2):
    matrixOfMulti = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
    for row in range(len(matrixOfMulti)):
        for column in range(len(matrixOfMulti[row])):
            multi_num = 0
            for room in range(len(matrix_1[0])):
                multi_num = multi_num + (matrix_1[row][room] * matrix_2[room][column])
                #print("Room = ", room, "Row = ", row, "Column = ", column, "multi_num = ", multi_num,"matrix_1 = ",matrix_1[row][room],"matrix_2 = ", matrix_2[room][column], "\n")
            matrixOfMulti[row][column] = multi_num
        
    return matrixOfMulti

def matrixTranspose (matrix_1):
    matrixOfTranspose = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
    for row in range(len(matrix_1)):
        for column in range(len(matrix_1[row])):
            matrixOfTranspose[row][column] = (matrix_1[column][row])
    return matrixOfTranspose

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1],[2],[3]]



#x = [[1,2,3],[4,5,6]] 
#y = [[1,2,3],[4,5,6],[7,8,9]]

print(matrixMultipication(x, y))