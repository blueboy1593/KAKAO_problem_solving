# 핵심은 중복적으로 하나하나 세는 것을 방지하는거일걸.
import sys
sys.setrecursionlimit(10000)
# return을 2개를 해주는 문제. union find 개념이라고??? 내가 썼던 list랑 개념은 거의 비슷한데.. dict를 활용해야하나봐

def find_room(room, checkIn):
    if room not in checkIn:
        checkIn[room] = room + 1
        return room
    
    save_room = find_room(checkIn[room], checkIn)
    checkIn[room] = save_room + 1
    return save_room

def solution(k, room_number):
    answer = []
    checkIn = {} # 여유분을 하나 만들어두면 하나씩 로직 절약 가능할듯.
    for room in room_number:
        checked_room = find_room(room, checkIn)
        answer.append(checked_room)
        # if checkIn[room] == 0:
        #     answer.append(room)
        #     checkIn[room] = room + 1 # 비어있는 최대라는거징!
        #     continue
        # else:
        #     stack = []
        #     next_room = checkIn[room]
        #     while True:
        #         if checkIn[next_room] == 0:
        #             checkIn[next_room] = next_room + 1
        #             answer.append(next_room)
        #             for s in stack:
        #                 checkIn[s] = next_room
        #             stack = []
        #             break
        #         else:
        #             stack.append(next_room)
        #             next_room += 1

    # print(answer)
    return answer

solution(10, [1,3,4,1,3,1])