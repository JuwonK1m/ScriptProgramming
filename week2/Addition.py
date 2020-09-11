# 초등학생을 위한 덧셈 퀴즈 프로그램

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
result = number1 + number2

answer = eval(input(str(number1) + " + " + str(number2) + "은 얼마입니까? >> "))

if (result == answer):
    print("맞았습니다")
else:
    print("틀렸습니다")