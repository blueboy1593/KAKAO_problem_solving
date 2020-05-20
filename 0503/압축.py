# 사전은 아마 dict로 구현하는 거겠지.
# 쉬운거같은데?? 아마 dictionary 사용법을 아는지 물어보는 문제.
# dict를 조금 응용할 줄 알고, 다음으로 넘어가는 임시 스택? 느낌.
# dict의 value에 접근하는거 한번 찾아는 봐야지. 근데 in 같은걸 써야겠지 아무래도??

def solution(msg):
    answer = []
    kakaopedia = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    n = 27
    j_stop = 0
    for i in range(len(msg)):
        if i < j_stop:
            continue
        temp = msg[i]
        # print(i)
        for j in range(i + 1, len(msg)):
            temp2 = temp + msg[j]
            # print(temp2)
            if not kakaopedia.get(temp2):
                kakaopedia[temp2] = n
                n += 1
                j_stop = j
                break
            temp = temp2
        answer.append(kakaopedia[temp])
        if j_stop == len(msg) - 1:
            continue
        # 음.... 이걸로? ㅋㅋㅋ
        if j == len(msg) - 1:
            break
    # print(answer)
    return answer
# 여기서 해보고 싶었던게 있어!

solution('TOBEORNOTTOBEORTOBEORNOT')

# 좀 돌아서 하느라 43분이나 걸렸어.

# tmp = {chr(e + 64): e for e in range(1, 27)} 이거로 알파벳 딕트 만든다.