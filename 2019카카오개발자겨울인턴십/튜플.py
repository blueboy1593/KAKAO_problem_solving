# LEVEL2인데 너무 쉬운거 아냐??
# DP처럼 시간을 좀 생각해줘야 하나?
# 문자열을 다루어야함.

# 이게 확실한 블로그!!!
# Dictionary 값 value 로 정렬하기
# 사전의 value 값으로 정렬하는 방법은 sorted 함수를 사용합니다.
# sorted 함수는 key 를 받을 수 있는데, 여기서 lambda 식을 사용하여 튜플에서 1 번째 index를 기준으로 정렬하는 것 이지요
# >>> d = {'A': 3, 'C': 1, 'G': 5, 'T': 2}
# >>> d
# {'A': 3, 'C': 1, 'G': 5, 'T': 2}
 
# ## d.items() 를 하여 각 key, value 가 tuple로 들어있는 
# ## 리스트 (dict_items 객체) 로 만듭니다
# >>> d.items()
# dict_items([('A', 3), ('C', 1), ('G', 5), ('T', 2)])
 
# ## dict_items 객체를 lambda 식을 활용하여 정렬을 하는 거지요 
 
# ## 오름차순 정렬
# >>> sorted(d.items(), key=lambda x: x[1])
# [('C', 1), ('T', 2), ('A', 3), ('G', 5)]
 
# ## 내림차순 정렬
# >>> sorted(d.items(), key=lambda x: x[1], reverse=True)
# [('G', 5), ('A', 3), ('T', 2), ('C', 1)]
# 출처: https://korbillgates.tistory.com/171 [생물정보학자의 블로그]


def solution(s):
    answer = []
    set_dict = {}
    stack = ''
    for i in range(len(s)):
        if s[i].isdigit():
            stack += s[i]
        elif s[i] == '}' or s[i] == ',':
            if stack != '':
                int_stack = int(stack)
                if set_dict.get(int_stack):
                    set_dict[int_stack] += 1
                else:
                    set_dict[int_stack] = 1
                stack = ''
    
    nasus = set_dict.items()
    nasus = sorted(nasus, key=lambda x: x[1], reverse=True)
    for na in nasus:
        answer.append(na[0])

    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")