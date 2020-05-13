# 순열조합 문제?? 인지는 모르겠는데, 순열식으로 한번 해보장!
# 1개짜리는 우선적으로 빼버릴까...?
# list는 set이 안된다는 거지...
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
        for k in range(kk + 1, pre_combs_leng):
            kj = pre_combs[k]
            for i in range(row):
                arr[i].append(relation[i][kj])
            print(arr)
            if len(arr) == len(set(arr)):
                answer += 1
                continue
            else:
                find_hubokey(k + 1, arr)


    pre_combs_leng = len(pre_combs)
    # 이거 굳이 할 필요가 없나...? 아냐 해야해. 왜냐면 치트키가 될 수 있거든
    for k in range(pre_combs_leng):
        kj = pre_combs[k]
        kj_col = []
        for i in range(row):
            kj_col.append([relation[i][kj]])
        print(kj_col)
        find_hubokey(k, kj_col)

    return answer


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])