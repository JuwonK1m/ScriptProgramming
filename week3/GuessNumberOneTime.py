# 컴퓨터가 임의로 생성한 숫자를 맞히는 게임
# 0 이상 100 이하 사이 정수를 랜덤하게 생성
# 생성된 숫자가 사용자의 입력 숫자와 일치할 때까지 계속 입력 받음
# 각 사용자 입력에 대해, 생성 숫자보다 큰지, 작은지 응답하여 사용자가 지능적으로 다음 숫자를 입력을 할 수 있게 함

import random

num = random.randint(0, 100)

answer = eval(input("추측하시오 (0 ~ 100인 정수)>> "))

while num != answer:
    if num > answer:
        print("입력한 숫자보다 더 큽니다.")
    else:
        print("입력한 숫자보다 더 작습니다.")
        
    answer = eval(input("추측하시오 (0 ~ 100인 정수)>> "))
    
print(str(num) + "이(가) 정답이었습니다.")