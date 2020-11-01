from random import randrange

matrix = []

rows = eval(input("행 입력: "))
cols = eval(input("열 입력: "))

for row in range(0, rows):
    matrix.append([])
    for col in range(0, cols):
        matrix[row].append(randrange(0, 100))
        
print(matrix)