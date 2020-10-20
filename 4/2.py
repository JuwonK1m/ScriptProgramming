from random import randint

A = [None] * 10
cnt = [0] * 11

for i in range(0, len(A)):
    A[i] = randint(0, 10)
    cnt[A[i]] += 1
    
print("A =", A)

for i in range(0, len(cnt)):
    if cnt[i] >= 2:
        for j in range(0, cnt[i] - 1):
            A.remove(i)
            
A.sort()
            
print("A =", A)