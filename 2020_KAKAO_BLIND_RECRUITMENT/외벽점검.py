def solution(n, weak, dist):
    answer = [float('inf')]
    outer_wall = [ 1 ] * n
    for i in range(len(weak)):
        outer_wall[weak[i]] = 0
    dist.sort(reverse=True)
    print(outer_wall)
    visited = [ False ] * len(dist)

    def change_num(num):
        return num % n

    dist_len = len(dist)
    weak_len = len(weak)
    def clean_outer_wall(cnt):
        if outer_wall == [ 1 ] * n:
            answer[0] = min(answer[0], cnt)
            return
        for k in range(dist_len):
            if visited[k] == False:
                visited[k] = True
                for i in range(weak_len):
                    if outer_wall[weak[i]] == 0:
                        start = weak[i]
                        end = weak[i] + dist[k]
                        stack = []
                        for j in range(start, end + 1):
                            j = change_num(j)
                            # print(j)
                            if outer_wall[j] == 0:
                                stack.append(j)
                        # for we in weak:
                        #     if start <= we <= end:
                        #         if outer_wall[we] == 0:
                        #             stack.append(we)
                        stack2 = stack[:]
                        for st in stack2:
                            outer_wall[st] = 1
                        clean_outer_wall(cnt + 1)
                        for st in stack2:
                            outer_wall[st] = 0
                        # 흠... 이거 좀 이상하기는 하다. 재활용보다 새로 하는게 나을 듯. 이 문제에서는.
                visited[k] = False
    clean_outer_wall(0)
    if answer == [float('inf')]:
        return -1
    return answer[0]

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])