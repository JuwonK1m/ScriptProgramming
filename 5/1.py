from random import randint

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("%3d"%(matrix[i][j]), end = '')
        print()

matrix = []

n = eval(input("n을 입력하시오: "))

for i in range(0, n):
    matrix.append([])
    for j in range(0, n):
        matrix[i].append(randint(0, 1))
        
printMatrix(matrix)
print()
    
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == 0:
            matrix[i][j] = -1
            
printMatrix(matrix)