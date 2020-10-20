from random import randint

A = [None] * 20

for i in range(0, len(A)):
    A[i] = randint(-10, 10)
    
print("A =", A)
print("음수인덱스: ", end = "")
first = True
for i in range(0, len(A)):
    if A[i] < 0: 
        if first:
            print(i, end = "")
            first = False
        else:
            print(",", i, end = "")
        A[i] *= -1
print()
print("A =", A)  