# 구구단 표 출력 프로그램

print("  |", end = '')
for i in range(1, 10):
    print("  ", i, end = '')
print()
print("------------------------------------------")

for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        print(format(i * j, '4d'), end = '')
    print()
        