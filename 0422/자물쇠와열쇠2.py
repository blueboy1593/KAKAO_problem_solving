def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    key2 = [ [0] * M for _ in range(M) ]
    key3 = [ [0] * M for _ in range(M) ]
    key4 = [ [0] * M for _ in range(M) ]
    for i in range(M):
        for j in range(M):
            key2[j][M - 1 - i] = key[i][j]

    for i in range(M):
        for j in range(M):
            key3[j][M - 1 - i] = key2[i][j]

    for i in range(M):
        for j in range(M):
            key4[j][M - 1 - i] = key3[i][j]

    key_set = [key, key2, key3, key4]
    for key in key_set:
        # print(*key, sep='\n')
        for i2 in range(N - M + 1, 2*N):
            for j2 in range(N - M + 1, 2*N):
                # 얘는 반복으로 넣어도 좋지
                # deepcopy 매번 해주기.
                lock2 = [ [0] * (3*N) for _ in range(3*N) ]
                for i in range(N):
                    for j in range(N):
                        lock2[N + i][N + j] = lock[i][j]
                # key를 여기에 넣어보는 logic
                for i in range(M):
                    for j in range(M):
                        lock2[i2 + i][j2 + j] += key[i][j]
                
                check = True
                for i in range(N):
                    for j in range(N):
                        if lock2[N + i][N + j] != 1:
                            check = False
                            break
                    if check == False:
                        break
                if check == True:
                    return True
    # print(*key, sep='\n')
    # print(*key2, sep='\n')
    # print(*key3, sep='\n')
    # print(*key4, sep='\n')

    return answer



solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])