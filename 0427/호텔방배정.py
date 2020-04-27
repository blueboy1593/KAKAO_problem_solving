# 핵심은 중복적으로 하나하나 세는 것을 방지하는거일걸.
import sys

def solution(k, room_number):
    answer = []
    checkIn = [0] * (k + 1 + 1) # 여유분을 하나 만들어두면 하나씩 로직 절약 가능할듯.
    for room in room_number:
        if checkIn[room] == 0:
            answer.append(room)
            checkIn[room] = room + 1 # 비어있는 최대라는거징!
            continue
        else:
            stack = []
            next_room = checkIn[room]
            while True:
                if checkIn[next_room] == 0:
                    checkIn[next_room] = next_room + 1
                    answer.append(next_room)
                    for s in stack:
                        checkIn[s] = next_room + 1
                    stack = []
                    break
                else:
                    stack.append(next_room)
                    next_room = checkIn[next_room] # 좀 바꾼 로직
                    # 이거로 먹여줘야지, +1 로 하면 아까랑 다를게 없지
    # print(answer)
    return answer

solution(10, [1,3,4,1,3,1])