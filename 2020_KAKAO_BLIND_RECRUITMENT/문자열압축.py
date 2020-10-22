# 알고리즘 자체는 쉬운 것 같은데, 문제를 이해하는데 시간이 좀 걸린다.

def solution(s):
    answer = len(s)
    L = len(s)
    half = L // 2
    # 1부터 반에 해당하는 숫자까지 차례차례 트라이.
    for n in range(1, half + 1):
        cnt = 0
        temp = []
        stack = []
        for i in range(L):
            temp.append(s[i])
            cnt += 1
            if cnt == n:
                cnt = 0
                stack.append(temp)
                temp = []
        if temp != []:
            stack.append(temp)
        print(stack)
        # 첫 관문인 stack은 무사히 만들었다. 이제 비교해야지
        tem = stack[0]
        cnt = 1
        temp_answer = ''
        for i in range(1, len(stack)):
            if stack[i] == tem:
                cnt += 1
            else:
                # 이거는 파이썬에서 문자열 다루는 실력이지!
                if cnt > 1:
                    temp_answer += str(cnt) + ''.join(map(str, tem))
                else:
                    # cnt가 2 이상일 때에만 cnt를 같ㅇ이 출력한다.
                    temp_answer += ''.join(map(str, tem))
                tem = stack[i]
                cnt = 1
        if cnt > 1:
            temp_answer += str(cnt) + ''.join(map(str, tem))
        else:
            temp_answer += ''.join(map(str, tem))
        # 여기는 마지막에 남는 애까지 완벽하게 처리해주는 곳

        # 최소값 찾아주는 로직
        answer = min(answer, len(temp_answer))
    return answer

solution("aabbaccc")