def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for mo in moves:
        for i in range(N):
            if board[i][mo - 1] != 0:
                if stack == []:
                    stack.append(board[i][mo - 1])
                elif stack[-1] == board[i][mo - 1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][mo - 1])
                board[i][mo - 1] = 0
                break
                
    return answer


# 바꾼게 하나밖에 없는데 시간차이는 꽤 난다.
def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for mo in moves:
        mo -= 1
        for i in range(N):
            if board[i][mo] != 0:
                if stack == []:
                    stack.append(board[i][mo])
                elif stack[-1] == board[i][mo]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][mo])
                board[i][mo] = 0
                break
                
    return answer