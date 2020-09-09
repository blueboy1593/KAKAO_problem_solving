# 1. 재귀 or (dictionary or list) 매칭을 통해 불량 사용자 리스트 만들기
# 2. 정렬 후 set에 넣어 중복 제거 

def solution(user_id, banned_id):
    answer = 0
    user_len = len(user_id)
    banned_len = len(banned_id)

    # 1번 불량 사용자인지 비교 
    def check_id(user, banned):
        if len(user) != len(banned):
            return False
        for k in range(len(user)):
            if banned[k] == '*':
                continue
            if user[k] != banned[k]:
                return False
        return True

    # 2번 재귀를 통해 전체 리스트 만들기
    total_users = set()
    user_stack = []
    def match(i):
        if i == banned_len:
            total_users.add(tuple(sorted(user_stack[:])))
            return
        ban_id = banned_id[i]
        for j in range(user_len):
            if user_id[j] not in user_stack: # 현재 스택에 중복되어 있는지.
                if check_id(user_id[j], banned_id[i]): # 불량 사용자와 매치가 되는지
                    user_stack.append(user_id[j])
                    match(i + 1)
                    user_stack.pop()
    match(0)

    answer = len(total_users)
    return answer