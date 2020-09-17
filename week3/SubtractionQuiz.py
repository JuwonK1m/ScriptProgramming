import random

a = random.randint(0, 9)
b = random.randint(0, 9)
result = a - b

print(str(a) + " - " + str(b) + " = ?")
answer = eval(input("입력하시오 >> "))
print()

while result != answer: 
    print("틀렸습니다. 다시 시도하십시오.")
    print(str(a) + " - " + str(b) + " = ?")
    answer = eval(input("입력하시오 >> "))
    print()

print("정답입니다.")