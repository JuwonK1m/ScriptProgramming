fruits_dic = {"apple":6000, "melon":3000, "banana":5000, "orange":4000}

print("딕셔너리의 키는")
print(list(fruits_dic.keys()))

print("딕셔너리의 값은")
print(list(fruits_dic.values()))

while True:
    fruit = input("검사하고 싶은 과일은? ")
    if fruit == "":
        break
    if fruits_dic.get(fruit) == None:
        print("해당 과일은 없습니다.")
    else:
        print("해당 과일은 있습니다.")
    
print("종료합니다.")