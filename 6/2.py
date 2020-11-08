sales = [(100, 90), (115,100), (85, 103), (64,105), (124,60)]

A_cnt = 0 # A 매장 전날 대비 매출 감소 일
B_cnt = 0 # B 매장 전날 대비 매출 감소 일
A = [] # A 매장 전날 대비 매출 감소 요일 리스트
B = [] # B 매장 전날 대비 매출 감소 요일 리스트

for i in range(0, len(sales) - 1):
    if sales[i][0] > sales[i + 1][0]:
        A_cnt += 1
        if i + 1 == 1:
            A.append("화요일")
        if i + 1 == 2:
            A.append("수요일")
        if i + 1 == 3:
            A.append("목요일")
        if i + 1 == 4:
            A.append("금요일")
    if sales[i][1] > sales[i + 1][1]:
        B_cnt += 1
        if i + 1 == 1:
            B.append("화요일")
        if i + 1 == 2:
            B.append("수요일")
        if i + 1 == 3:
            B.append("목요일")
        if i + 1 == 4:
            B.append("금요일")
    
print("A매장 전날 대비 매출 감소 일: {}일".format(A_cnt))
print("B매장 전날 대비 매출 감소 일: {}일".format(B_cnt))
print("A 매장 전날 대비 매출 감소 요일: ", end = '')
for i in A: print(i, end = ' ')
print()
print("B 매장 전날 대비 매출 감소 요일: ", end = '')
for i in B: print(i, end = ' ')
print()