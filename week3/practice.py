# 연, 월, 일을 입력받아 ####-##-##의 형태로 출력하는 프로그램을 작성하시오. 
# 단, 월과 일에 1~9의 숫자가 입력되면 그 숫자 앞에 0을 채운다.

year = input("연을 입력하세요: ")
month = eval(input("월을 입력하세요: "))
day = eval(input("일을 입력하세요: "))

#print(year + "-", end = "")

#if month < 10:
#    print("0" + str(month) + "-", end = "")
#else:
#    print(str(month) + "-", end = "")
    
#if day < 10:
#    print("0" + str(day))
#else:
#    print(day)

print(str(year) + "-" + str(format(month, "02d")) + "-" + str(format(day, "02d")))