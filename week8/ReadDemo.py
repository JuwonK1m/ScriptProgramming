infile = open("lectures.txt", "r")
print("read() 사용하기")
print(infile.read())
infile.close()

infile = open("Lectures.txt", "r")
print("read(number) 사용하기")
print(infile.read(9))

infile = open("Lectures.txt", "r")
print("readline() 사용하기")
print(infile.readline())
print(infile.readline())
print(infile.readline())

infile = open("Lectures.txt", "r")
print("readlines() 사용하기")
print(infile.readlines())