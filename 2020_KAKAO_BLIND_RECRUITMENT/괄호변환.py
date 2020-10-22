# 문제 이해하는게 넘 짜증나!
# 재귀 함수가 꼭 들어가야 하는구나.
# 재귀 함수는 return이 안먹히는데???
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 이거 괜히 준게 아니고, 재귀에서도 return 먹히기는 하네....

def arrange(u):
    if len(u) == 2:
        return ''
    else:
        uu = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                uu += ')'
            else:
                uu += '('
        return uu

def divide_UV(p):
    if p == '':
        return ''
    cnt1 = 0 # (
    cnt2 = 0 # )
    stack = ''
    check_balanced = True

    for i in range(len(p)):
        stack += p[i]
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 < cnt2: # 한번이라도 저 짝대기가 많이 나왔으면 불균형일 것.(추측)
            check_balanced = False
        if cnt1 == cnt2: # 불균형인 조건이 들어가야함
            u = stack
            v = p[i + 1:]  # slice 쓰는 연습!!
            # print("v:", v) # 이거 좋았따
            if check_balanced == True:
                new_v = divide_UV(v)
                # print(u, new_v)
                return u + new_v
            else:
                # 불균형 판단 함수 만들기
                # will_add = arrange(stack)
                # answer += ''.join(map(str, will_add))
                # 이건 버려. 문제 읽은대로 하자
                temp = '('
                new_v = divide_UV(v)
                temp += new_v
                temp += ')'
                new_u = arrange(u)
                temp += new_u
                return temp
    # 어떤 값이라도 return을 꼭 해주는 조건이 있으면 재귀에서도 return이 먹기는 하는구나. Good!!!

def solution(p):
    answer = divide_UV(p)
    return answer


solution("()))((()")