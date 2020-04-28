# isalpha랑 capitalize하는거 그거 사용하면 될거같은데

def str_list(string):
    arr = []
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            arr.append(string[i].capitalize() + string[i + 1].capitalize())
    return arr

def solution(str1, str2):
    answer = 0
    # 1단계. input 들어온 것을 집합으로 나눠서 표현!
    # set은 내가 알기론 중복된 원소가 없어서 list로 해야할듯?
    arr1 = str_list(str1)
    arr2 = str_list(str2)
    # print(arr1, arr2)

    AnB = []
    AuB = []
    for ar in arr1:
        if ar in arr2: # 둘 다 있을때! 
            arr2.remove(ar)
            AnB.append(ar)
            AuB.append(ar)
        else:
            AuB.append(ar)
    for ar2 in arr2:
        AuB.append(ar2)
    # print(AnB, AuB)
    if AuB == []:
        answer = 65536
    else:
        temp_ans = float(len(AnB)/len(AuB)) * 65536
        answer = int(temp_ans)
    return answer


solution("FRANCE", "french")
# 28분...