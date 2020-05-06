# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고, # 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다. e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)] f = sorted(e, key = lambda x : (x[0], -x[1])) # f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]
# 궁금증: 람다를 쓰지 않는다면...?

def solution(N, stages):
    answer = []
    N_cleared = [0] * (N + 1)
    N_notcleared = [0] * (N + 2)
    for s in stages:
        for i in range(1, s):
            N_cleared[i] += 1
            N_notcleared[i] += 1
        N_notcleared[s] += 1
    failure_late = []
    # print(N_cleared)
    # print(N_notcleared)

    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다. 이게 은근 어려운거같은데
    for n in range(1, N + 1):
        # 이거는 런타임 에러 잡아주는 것!!!
        if N_notcleared[n] != 0:
            failure_late.append((n, (N_notcleared[n] - N_cleared[n])/N_notcleared[n]))
    # print(failure_late)
    n_rate = sorted(failure_late, key=lambda x: (-x[1], x[0]))

    for nn in n_rate:
        answer.append(nn[0])
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])