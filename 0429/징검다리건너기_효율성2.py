# 처음에 0이 없이 dict 구성을 하던가, 아니면 중간에 0 이하로 내려갔을 때 빼주던가.
# 시간이 오래걸리는데 짬이 없었으면 이것보다 더 걸리거나 아예 못풀었을걸??

def solution(stones, k):
    answer = 0
    len_stones = len(stones)
    stones_dict = dict()
    # 여기 확실히 문제가 있어보인다.
    initi = 0
    for i in range(len_stones):
        if stones[i] > 0:
            stones_dict[initi] = i + 1
            initi = i + 1
    # 마지막 숫자 작업을 해야하네
    stones_dict[initi] = len_stones + 1
    # print(stones_dict)
    stones.append(-1)

    # def start_with_zero(num):
    # start_with_zero(0)
    flag = False
    while True:
        num = 0
        while num <= len_stones:
            target = stones_dict[num]
            # 징검다리를 못건너는 상황이면!!
            if target - num > k:
                flag = True
                break
            while True:
                stones[target - 1] -= 1
                # 여기 중간에 널뛰기가 되는 반례 생각해야해
                if stones[target - 1] == 0:
                    temp_target = stones_dict[target]
                    if temp_target - target > k:
                        flag = True
                        target = len_stones + 1
                        break
                    else:
                        target = temp_target
                else:
                    break
            stones_dict[num] = target
            num = target
        if flag == True:
            break
        answer += 1
    # print(stones_dict)
    # print(answer)
    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)