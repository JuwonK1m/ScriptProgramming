# 입력한 두 정수의 최대공약수를 찾는 프로그램

n1 = eval(input("n1을 입력하시오: "))
n2 = eval(input("n2을 입력하시오: "))

gcd = 1

i = 2
while i <= n1 and i <= n2:
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
    i = i + 1
    
print(str(n1) + "와(과) " + str(n2) + "의 최대공약수는 " + str(gcd) + "입니다.")