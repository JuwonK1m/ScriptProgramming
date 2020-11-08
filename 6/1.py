dic = {}
amount = 0

while True:
    item = input("구매 품목: ")
    if item == "":
        break
    price = eval(input("가격: "))
    quantity = eval(input("수량: "))
    dic[item] = [price, quantity, price * quantity]
    
for key in dic:
    print("{} {} 원 * {}개 = {}원".format(key, dic[key][0], dic[key][1], dic[key][2]))
    amount += dic[key][2]
    
print("총 지불액: {}원".format(amount))