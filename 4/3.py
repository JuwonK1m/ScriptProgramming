from random import randint

A = [True] * 10
x = [None] * 10
y = [None] * 10

for i in range(0, len(A)):
    randVal1 = randint(0, 1)
    randVal2 = randint(0, 1)
    if randVal1 == 0:
        x[i] = False
    else:
        x[i] = True
    if randVal2 == 0:
        y[i] = False
    else:
        y[i] = True
        
print("A =", A)
print("x =", x)
print("y =", y)

for i in range(0, len(A)):
    if x[i] == False and y[i] == False:
        A[i] = False
        
print("A= ", A)