def solution(stones, k):
    stones_len = len(stones)
    l_pivot = 0
    r_pivot = 200000000

    # 1번. 돌덩이 지나갈 수 있는지 없는지 체크
    def check_niniz(pivot):
        temp = 0
        for stone in stones:
            if stone < pivot:
                temp += 1
                if temp >= k:
                    return False
            else:
                temp = 0
        return True

    # 2번. 이분탐색 구간 pivot 조절
    while True:
        mid_pivot = (l_pivot + r_pivot) // 2
        if mid_pivot == l_pivot: # 만약 이분탐색을 더이상 진행할 수 없다면 바로 답 return
            return l_pivot
        if check_niniz(mid_pivot) == True:
            l_pivot = mid_pivot
        else:
            r_pivot = mid_pivot

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))