def solution(board):
    answer = 0
    N = len(board)
    visited = [ [float('inf')] * N for _ in range(N) ]
    visited[0][0] = 0
    visited[1][0] = 100
    visited[0][1] = 100

    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def direction_set(d):
        if 0 <= d <= 3:
            return d
        if d == -1:
            return 3
        if d == 4:
            return 0
    
    def isWall(y, x):
        if 0 <= x < N and 0 <= y < N:
            if board[y][x] == 0:
                return True
        else:
            return False

    # i, j, direction, 거리값
    queue = [(0, 0, 0, 0), (0, 0, 1, 0)]
    while queue:
        # 여기서 heap을 사용하면 가장 최적의 값부터 시도할 수도 있겠지?
        que = queue.pop(0)
        i, j, d, price = que
        # 직진 로직
        idy = i + D[d][0]
        jdx = j + D[d][1]
        if isWall(idy, jdx):
            # visited에 저장해둔 값을 함부로 쓰면 혼선이 생길 수 있기 때문에, 가지고 다녀야 할듯 하다.
            if price + 100 < visited[idy][jdx] + 500: # 이거 쪼금 위험해. 헷갈려.
                visited[idy][jdx] = min(price + 100, visited[idy][jdx]) # visited는 더 작은 값으로 해줘야함.
                queue.append((idy, jdx, d, price + 100))

        # 곡선으로 가는 로직 1번
        d1 = direction_set(d + 1)
        idy = i + D[d1][0]
        jdx = j + D[d1][1]
        if isWall(idy, jdx):
            if price + 500 < visited[idy][jdx] + 500:
                visited[idy][jdx] = min(price + 600, visited[idy][jdx])
                queue.append((idy, jdx, d1, price + 600))
        # 곡선으로 가는 로직 2번
        d2 = direction_set(d - 1)
        idy = i + D[d2][0]
        jdx = j + D[d2][1]
        if isWall(idy, jdx):
            if price + 500 < visited[idy][jdx] + 500:
                visited[idy][jdx] = min(price + 600, visited[idy][jdx])
                queue.append((idy, jdx, d2, price + 600))
        
    answer = visited[N - 1][N - 1]
    return answer

solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])