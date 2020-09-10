# from copy import deepcopy

def solution(key, lock):
    N = len(lock)
    M = len(key)

    # 1번 전체 맵 3N 사이즈로 재구성하기.
    lock_map = [ [0] * 3*N for _ in range(3*N) ]
    for i in range(N):
        for j in range(N):
            lock_map[N + i][N + j] = lock[i][j]
    # 프린트로 만든거 꼭 확인해보기
    # print(*lock_map, sep='\n')

    # 2번 90도 회전하는 함수 만들기
    def rotate(arr):
        return list(zip(*arr[::-1]))
    # 꼭 다시 시험해봐야 한다.
    # print(*key, sep='\n')
    # print(*rotate(key), sep='\n')

    # 3번. 4번동안 key 돌려가면서, N - M + 1 부터 2N - 1까지 시도하기. copy로 시도
    for _ in range(4):
        # copied_map = deepcopy(lock_map) 카피는 보류하자.
        
        for i in range(N - M + 1, 2*N):
            for j in range(N - M + 1, 2*N):
                # 자물쇠에 key를 더해주는 로직
                for ii in range(M):
                    for jj in range(M):
                        lock_map[i + ii][j + jj] += key[ii][jj]
                
                # 열쇠가 잠겼는지 확인
                flag = True
                for y in range(N, 2*N):
                    for x in range(N, 2*N):
                        if lock_map[y][x] != 1:
                            flag = False
                            break
                    if flag == False:
                        break
                if flag == True:
                    return True
                
                # 다시 자물쇠에서 key 빼주기
                for ii in range(M):
                    for jj in range(M):
                        lock_map[i + ii][j + jj] -= key[ii][jj]
        
        # 열쇠 사용 후, 90도 회전 해주기.
        key = rotate(key)
    return False