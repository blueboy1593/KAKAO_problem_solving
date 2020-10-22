# 어렵지 않은거같아. 3가지 케이스로 나누면 될거같아.
# 1번 옆으로 2개 이어진거, 2번 옆으로 1칸 띄어진거, 3번 세로로 2개 이어진거.
# while과 flag로 하면 될 것 같다.
# 이번 문제에서 isWall을 하지 않기 위해 -1로 벽을 둘러싸는거 연습해보자!
# 1시간 40분만에 인간승리...
# 피드백을 좀 해야해. 맨 위 블록을 신경을 안썼어.

def solution(board):
    answer = 0

    # 0번. iswall 하지 않기 위해 -1로 벽 둘러싸기.
    N = len(board)
    new_board = [ [0] * (N + 2) for _ in range(N + 2) ]
    for i in range(N + 2):
        new_board[i][0] = -1
        new_board[i][N + 1] = -1
    for j in range(N + 2):
        new_board[0][j] = -1
        new_board[N + 1][j] = -1
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]
    # 이거보다 코드 줄일 수 있는 방법이 있겠지?
    # print(*new_board, sep='\n')

    def func1(j):
        if new_board[1][j] != 0 or new_board[1][j + 1] !=0: # 과연...? 이게..?
            return False
        for i in range(1, N):
            if new_board[i + 1][j] > 0 or new_board[i + 1][j + 1] > 0: # 이거 조건 안넣어주면 안되징.
                if new_board[i + 1][j] == new_board[i + 1][j + 1] and new_board[i][j] == 0 and new_board[i][j + 1] == 0:
                    # 왼쪽 2개 확인
                    if new_board[i + 1][j] == new_board[i + 1][j - 1] == new_board[i][j - 1]:
                        new_board[i + 1][j] = 0
                        new_board[i + 1][j + 1] = 0
                        new_board[i + 1][j - 1] = 0
                        new_board[i][j - 1] = 0
                        return True
                    if new_board[i + 1][j] == new_board[i + 1][j + 2] == new_board[i][j + 2]:
                        new_board[i + 1][j] = 0
                        new_board[i + 1][j + 1] = 0
                        new_board[i + 1][j + 2] = 0
                        new_board[i][j + 2] = 0
                        return True
                break

    def func2(j):
        if new_board[1][j] != 0 or new_board[1][j + 2] !=0:
            return False
        for i in range(1, N):
            if new_board[i + 1][j] > 0 or new_board[i + 1][j + 2] > 0:
                if new_board[i][j] == 0 and new_board[i][j + 2] == 0:
                    if new_board[i][j + 1] == new_board[i + 1][j] == new_board[i + 1][j + 2] == new_board[i + 1][j + 1]:
                        new_board[i][j + 1] = 0
                        new_board[i + 1][j] = 0
                        new_board[i + 1][j + 2] = 0
                        new_board[i + 1][j + 1] = 0
                        return True
                break

    def func3(j):
        # 블록 맨 위에 2개 확인하는게 주요했네... ㄷㄷ
        if new_board[1][j] != 0 or new_board[2][j] !=0:
            return False
        for i in range(1, N - 1):
            if new_board[i + 2][j] > 0:
                # if new_board[i][j] == new_board[i + 1][j] == 0:
                if new_board[i + 2][j] == new_board[i + 1][j - 1] == new_board[i][j - 1] == new_board[i + 2][j - 1]:
                    new_board[i + 2][j] = 0
                    new_board[i + 1][j - 1] = 0
                    new_board[i][j - 1] = 0
                    new_board[i + 2][j - 1] = 0
                    return True
                if new_board[i + 2][j] == new_board[i + 1][j + 1] == new_board[i][j + 1] == new_board[i + 2][j + 1]:
                    new_board[i + 2][j] = 0
                    new_board[i + 1][j + 1] = 0
                    new_board[i][j + 1] = 0
                    new_board[i + 2][j + 1] = 0
                    return True
                break

    flag = True
    while flag == True:
        flag = False
        # 1번. 2개 붙은거 함수 스코프 한번 시험해보자.
        for j in range(1, N):
            if func1(j) == True:
                answer += 1
                flag = True

        # 2번. 뻐큐모양 처리하기
        for j in range(1, N - 1):
            if func2(j) == True:
                answer += 1
                flag = True

        # 3번. 세로 2개 처리하기
        for j in range(1, N + 1):
            if func3(j) == True:
                answer += 1
                flag = True
    #     print('---------------------------------------------------')
    #     print(*new_board, sep='\n')
    # print('answer:', answer)
    return answer


solution([
    [0,0,0,0,0,0,0,0,6,0],
    [0,0,0,0,0,0,0,6,6,6],
    [0,0,0,0,0,0,0,0,0,0],
    [8,0,0,0,0,0,0,0,0,0],
    [8,0,0,0,0,0,4,0,0,7],
    [8,8,0,0,0,4,4,0,0,7],
    [0,9,0,0,3,0,4,0,7,7],
    [9,9,9,2,3,0,10,0,5,5],
    [1,2,2,2,3,3,10,0,0,5],
    [1,1,1,0,0,0,10,10,0,5]])
# solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])