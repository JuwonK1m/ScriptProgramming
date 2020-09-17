# 불특정 개수의 정수를 읽고 합계를 계산하는 프로그램

sum = 0

data = eval(input("정수를 입력하시오 (0을 입력하면 종료됩니다.) >> "))

while data != 0:
    sum += data
    data = eval(input("정수를 입력하시오 (0을 입력하면 종료됩니다.) >> "))
    
print("합계는 " + str(sum) + "입니다.")