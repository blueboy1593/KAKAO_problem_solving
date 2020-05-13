# 순열조합 문제?? 인지는 모르겠는데, 순열식으로 한번 해보장!
# 1개짜리는 우선적으로 빼버릴까...?
# list는 set이 안된다는 거지...
from copy import deepcopy
answer = 0

def solution(relation):
    global answer
    row = len(relation)
    col = len(relation[0])
    pre_combs = []
    for j in range(col):
        temp_col = []
        for i in range(row):
            temp_col.append(relation[i][j])
        if len(temp_col) != len(set(temp_col)):
            pre_combs.append(j)
        else:
            # 하나의 col만으로 유일키가 되면 정답 + 1 과 배제
            answer += 1

    # solution 안에 굳이 넣어보는 이유는, global이 어떻게 될 지 궁금해서.
    def find_hubokey(kk, arr):
        global answer
        for k in range(kk + 1, pre_combs_leng):
            kj = pre_combs[k]
            tuple_arr = deepcopy(arr)
            hanging_arr = deepcopy(arr)
            for i in range(row):
                tuple_arr[i].append(relation[i][kj])
                tuple_arr[i] = tuple(tuple_arr[i])
                hanging_arr[i].append(relation[i][kj])
            # append하고 tuple로 만들기까지 한다...
            # 너무 뻘짓거리 하는거같은데... ㅋㅋㅋ
            # print(tuple_arr)
            if row == len(set(tuple_arr)):
                answer += 1
                continue
            else:
                find_hubokey(k, hanging_arr)


    pre_combs_leng = len(pre_combs)
    # 이거 굳이 할 필요가 없나...? 아냐 해야해. 왜냐면 치트키가 될 수 있거든
    for k in range(pre_combs_leng):
        kj = pre_combs[k]
        kj_col = []
        for i in range(row):
            kj_col.append([relation[i][kj]])
        # print(kj_col)
        find_hubokey(k, kj_col)

    # print(answer)
    return answer


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
# 결국 모든 케이스를 구한다음에 contain? 이런 느낌의 함수를 쓰던가! 1, 2, 3, 4, 5 이런식으로 하자