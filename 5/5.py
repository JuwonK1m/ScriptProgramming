file = open("test_1.txt", "r", encoding='UTF8')

lines = file.readlines()

for i in range(0, len(lines)):
    print("{}  {}".format(i + 1, lines[i]))
    
file.close()