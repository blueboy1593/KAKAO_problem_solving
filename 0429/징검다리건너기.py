def solution(stones, k):
    answer = 0
    length = len(stones)
    flag = True
    while True:
        zero_stones = 0
        for i in range(length):
            if stones[i] > 0:
                zero_stones = 0
                stones[i] -= 1
            else:
                zero_stones += 1
                if zero_stones == k:
                    flag = False
                    break
        if flag == False:
            break
        answer += 1
    return answer