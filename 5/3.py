from random import randint

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("%-3d"%(matrix[i][j]), end = '')
        print()

matrix1 = []
matrix2 = []
matrix3 = []

n = eval(input("n을 입력하시오: "))

for i in range(0, n):
    matrix1.append([])
    matrix2.append([])
    matrix3.append([])
    for j in range(0, n):
        matrix1[i].append(randint(1, 9))
        matrix2[i].append(randint(1, 9))
        matrix3[i].append(None)

for i in range(0, n):
    for j in range(0, n):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        if matrix3[i][j] >= 10:
            matrix3[i][j] -= 10
        
printMatrix(matrix1)
print('+')
printMatrix(matrix2)
print('=')
printMatrix(matrix3)