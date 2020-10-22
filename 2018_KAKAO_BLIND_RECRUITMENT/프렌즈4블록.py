def solution(m, n, board):
    answer = 0
    board_map = [0] * m
    for i in range(m):
        board_map[i] = list(board[i])
    # print(board_map)

    stack = [0]
    while stack != []:
        stack = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board_map[i][j] == board_map[i + 1][j] == board_map[i][j + 1] == board_map[i + 1][j + 1] != 0: # 0은 아니어야 stack에 채우는 것을 멈춘당!
                    stack.append((i, j))
        # stack에 점 찍어둔 것 처리하기. 없어지는 갯수를 세어야해서 중복 주의
        for k in range(len(stack)):
            i, j = stack[k]
            for ii in range(2):
                for jj in range(2):
                    if board_map[i + ii][j + jj] != 0:
                        answer += 1
                    board_map[i + ii][j + jj] = 0

        # print(board_map)
        # 뿌요뿌요처럼 내리는 로직
        board_map2 = [ [ 0 ] * n for _ in range(m) ]
        for j in range(n):
            y = m - 1
            for i in range(m - 1, -1, -1):
                if board_map[i][j] != 0:
                    board_map2[y][j] = board_map[i][j]
                    y -= 1
        board_map = board_map2
        # 저번에 짠거랑은 좀 다른데 이것도 되겠지?
        # print(stack)

    # print(answer)
    return answer


solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])