def key_lock(key, lock):
    for i in range(N):
        for j in range(N):
            # 여기서 4개의 체킹 함수
            # 1번!
            # 나머지가 1인지 체크
            check_one = True
            for ii2 in range(i + 1, N):
                for jj2 in range(j + 1, N):
                    if lock[ii2][jj2] != 1:
                        check_one = False
                        break
                if check_one == False:
                    break
            # 검증하는 조건이 될 때 !
            if check_one == True:
                iii = M - 1
                check_two = True
                for ii in range(i, -1, -1):
                    jjj = M - 1
                    for jj in range(j, -1, -1):
                        if lock[ii][jj] + key[iii][jjj] != 1:
                            check_two = False
                            break
                        jjj -= 1
                    if check_two == False:
                        break
                    iii -= 1
                # 일련의 과정을 거쳐서 다 통과하면 참을 리턴...?
                if check_two == True:
                    return True
            
            # 2번 방향 로직
            check_one = True
            for ii2 in range(i + 1, N):
                for jj2 in range(j + 1, N):
                    if lock[ii2][jj2] != 1:
                        check_one = False
                        break
                if check_one == False:
                    break
            # 검증하는 조건이 될 때 !
            if check_one == True:
                iii = M - 1
                check_two = True
                for ii in range(i, -1, -1):
                    jjj = M - 1
                    for jj in range(j, -1, -1):
                        if lock[ii][jj] + key[iii][jjj] != 1:
                            check_two = False
                            break
                        jjj -= 1
                    if check_two == False:
                        break
                    iii -= 1
                # 일련의 과정을 거쳐서 다 통과하면 참을 리턴...?
                if check_two == True:
                    return True

                    


def solution(key, lock):
    answer = False
    N = len(lock)
    key2 = [ [0] * N for _ in range(N) ]
    key3 = [ [0] * N for _ in range(N) ]
    key4 = [ [0] * N for _ in range(N) ]
    



    for i in range(N):
        for j in range(N):
            key2[j][N - 1 - i] = key[i][j]

    for i in range(N):
        for j in range(N):
            key3[j][N - 1 - i] = key2[i][j]

    for i in range(N):
        for j in range(N):
            key4[j][N - 1 - i] = key3[i][j]

    # print(*key, sep='\n')
    # print(*key2, sep='\n')
    # print(*key3, sep='\n')
    # print(*key4, sep='\n')

    return answer



solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])