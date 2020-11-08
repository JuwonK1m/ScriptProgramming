s = set()

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            s.add((i, (j, k)))
            
print("3번의 주사위 실행 경우의 수")
print(sorted(s))