def matrixSum (matrix_1 ,matrix_2):
    try:
        if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
            matrixOfSum = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
            for row in range(len(matrix_2)):
                for column in range(len(matrix_2[row])):
                  matrixOfSum[row][column] = matrix_1[row][column] + matrix_2[row][column]
            return matrixOfSum
        else:
            print("There is sth wrong with the matrixes in matrixSum Function")
    except:
         print("There is an Unkown error in matrixSum Function")

          
def matrixSub (matrix_1 ,matrix_2):
    try:
        if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):  
            matrixOfSub = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
            for row in range(len(matrix_2)):
                for column in range(len(matrix_2[row])):
                  matrixOfSub[row][column] = matrix_1[row][column] - matrix_2[row][column]
            return matrixOfSub
        else:      
            print("There is sth wrong with the matrixes in matrixSub Function")
    except:
        print("There is an Unkown error in matrixSub Function")


def matrixScalar (matrix_1, k):
    try:
        matrixOfScalar = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
        for row in range(len(matrix_1)):
            for column in range(len(matrix_1[row])):
                matrixOfScalar[row][column] = (matrix_1[row][column] * k)
        return matrixOfScalar
    except:
        print("There is an Uknown error in matrixOfScalar Function")
        


def matrixMultiplication (matrix_1, matrix_2):
    try:
        if len(matrix_1[0]) == len(matrix_2) : 
            matrixOfMulti = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
            for row in range(len(matrixOfMulti)):
                for column in range(len(matrixOfMulti[row])):
                    multi_num = 0
                    for room in range(len(matrix_1[0])):
                        multi_num = multi_num + (matrix_1[row][room] * matrix_2[room][column])
                    matrixOfMulti[row][column] = multi_num
                
            return matrixOfMulti
        else:
            print("There is a problme with you matrixes in Multiplication part")
    except:
           print("There is an Unkown error in Multiplication for Matrixes")
            


def matrixTranspose (matrix_1):
    try:
        matrixOfTranspose = [[0 for _ in range (len(matrix_1[0]))] for _ in range (len(matrix_1))]
        for row in range(len(matrix_1)):
            for column in range(len(matrix_1[row])):
                matrixOfTranspose[row][column] = (matrix_1[column][row])
        return matrixOfTranspose
    except:
        print("There is an Uknown error with matrixOfTranspose Function")



x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1],[2],[3]]



#x = [[1,2,3],[4,5,6]] 
#y = [[1,2,3],[4,5,6],[7,8,9]]

print(matrixSum(x, y))