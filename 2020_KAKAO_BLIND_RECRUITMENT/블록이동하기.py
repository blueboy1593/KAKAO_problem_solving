# BFS or 다익스트라 문제
# 다익스트라로 중간중간 단계를 어떻게든 표현을 하거나,
# BFS로 겹치는 것이 있더라도 모든 경우의 수를 테스트하거나
# BFS는 visited로 하나씩만 방문할 때 썼던거라... 다익스트라를 해줘야할 것 같은데 ㅠㅠ



def solution(board):
    answer = 0
    # print(board)
    N = len(board)
    visited = [ [ [0,0] for _ in range(N) ] for _ in range(N) ] # 오우야! 이런식으로 3차원 배열 만드는 거구나.
    # visited[2][0][0] = 1
    # print(*visited, sep="\n")
    visited[0][1][0] = True
    print(*visited, sep="\n")

    # 이거로 작업하자
    def isWall(num):
        if 0 <= num < N:
            return True

    # 여기서부터 BFS 작업
    queue = [(0,1,0)] # y, x, 상태
    time = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            y, x, s = queue.pop(0)
            # 상하좌우 로직 들어가야겠지? s 상태에 따라서 다르게! 0은 -- 1은 ||
            if s == 0:
                if isWall(x + 1):
                    if visited[y][x + 1][0] == 0 and board[y][x + 1] == 0:
                        visited[y][x + 1][0] = True
                        queue.append((y, x + 1, 0))
                if isWall(x - 2):
                    if visited[y][x - 2][0] == 0 and board[y][x - 2] == 0:
                        visited[y][x - 2][0] = True
                        queue.append((y, x - 2, 0))




    return answer



solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])