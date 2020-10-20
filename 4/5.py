def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    l1 = list(s1)
    l2 = list(s2)
    for i in range(0, len(l1)):
        ch = l1[i]
        sameCharExist = False
        for j in range(0, len(l2)):
            if ch == l2[j]:
                l2.remove(ch)
                sameCharExist = True
                break
        if not sameCharExist:
            return False
    
    return True

s1 = input("1번째 문자열을 입력하시오: ")
s2 = input("2번째 문자열을 입력하시오: ")

if isAnagram(s1, s2):
    print("애너그램입니다.")
else:
    print("애너그램이 아닙니다.")