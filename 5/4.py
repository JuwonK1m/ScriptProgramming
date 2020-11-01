file = open("test_1.txt", "r", encoding='UTF8')

lines = file.readlines()

cnt = 0

for line in lines:
    words = line.split()
    for word in words:
        if word == "savage":
            print("Savage", end = ' ')
            cnt += 1
        else:
            print(word, end = ' ')
    print()
    
print()
print("savage는 {}번 등장합니다.".format(cnt))

file.close()