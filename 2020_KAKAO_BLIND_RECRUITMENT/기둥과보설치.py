# 배열의 크기를 2배로 만들어야 할까?
# 아니면 stack같은 거에 정보를 넣을까?
# 아마 둘 다 코드만 잘 짜면 가능은 할거야.
# 이번에는 배열을 2배로 해보자.
# 배열을 여유롭게 하는 것이 중요한 문제...

def solution(n, build_frame):
    answer = [[]]
    N = 2*n + 3
    mapp = [ [0] * (N) for _ in range(N) ]
    # 1열은 다 1로 처리해도 괜찮을거같아.
    for i in range(N):
        if i%2 == 1:
           mapp[1][i] = 1

    # 기둥: 2, 보: 3 으로 하자.
    for build in build_frame:
        # 정의해주기
        x, y, a, b = build # #################### 이거 나중에 꼭 변환
        # 총 4개의 case가 있을거야
        print(build)
        x = 2*x + 1
        y = 2*y + 1
        print(x, y, a, b)
        # 1번 기둥 설치
        if b == 1 and a == 0:
            if mapp[y][x] == 1: # 밑에 바칠것. 이거는 기본.
                if y == 1: # 바닥 위에 있는 경우
                    mapp[y + 1][x] = 2
                    mapp[y + 2][x] = 1
                elif mapp[y - 1][x] == 2: # 또 다른 기둥 위에 있는 경우
                    mapp[y + 1][x] = 2
                    mapp[y + 2][x] = 1
                elif x == 2*n: # 아래의 3개는 가장 어려운 1개보 위에 얹기.
                    if mapp[y][x - 1] == 3:
                        mapp[y + 1][x] = 2
                        mapp[y + 2][x] = 1
                elif x == 0:
                    if mapp[y][x + 1] == 3:
                        mapp[y + 1][x] = 2
                        mapp[y + 2][x] = 1
                else:
                    if mapp[y][x + 1] +mapp[y][x - 1] == 3: # 벽면을 넘어가지 않으니깐, 한칸 늘려도 되겠네...
                        mapp[y + 1][x] = 2
                        mapp[y + 2][x] = 1

        # 2번 보 설치
        elif b == 1 and a == 1:
            if mapp[y - 1][x] == 2 or mapp[y - 1][x + 2] == 2: # 둘중 하나가 기둥일떄!
                mapp[y][x] = 1
                mapp[y][x + 2] = 1
                mapp[y][x + 1] = 3
            elif mapp[y][x - 1] == 3 and mapp[y][x + 3] == 3: # 양쪽 끝이 다른 보와 연결되어 있을 때
                mapp[y][x] = 1
                mapp[y][x + 2] = 1
                mapp[y][x + 1] = 3

        # 3번 기둥 삭제
        elif a == 0 and b == 0:
            delete = True
            if mapp[y + 1][x] == 2: # 내 위에 기둥이 있는 경우
                if mapp[y][x + 1] + mapp[y][x - 1] != 3: # 아까의 충족조건이 갖춰진다면
                    delete = False
            elif mapp[y + 2][x - 1] == 3:
                


    print(*mapp, sep='\n')

    return answer

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])