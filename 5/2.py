def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("%-3d"%(matrix[i][j]), end = '')
        print()

val = 1
matrix = []

n = eval(input("n을 입력하시오: "))

for i in range(0, n):
    matrix.append([])
    if i % 2 == 0:
        for j in range(0, n):
            matrix[i].append(val)
            val += 1
    else:
        for j in range(0, n):
            matrix[i].append(None)
        for j in range(n - 1, -1, -1):
            matrix[i][j] = val
            val += 1
        
printMatrix(matrix)