# 그래프 느낌으로 가야하나? Dictionary JSON형태로 해보자.

def solution(words):
    answer = 0
    words_pedia = {}
    for word in words:
        if words_pedia.get(word[0]):
            start = words_pedia[word[0]]
        else:
            words_pedia[word[0]] = {}
            start = words_pedia[word[0]]
        for i in range(1, len(word)):
            if word[i] in start:
                pass
            else:
                start[word[i]] = {}
            start = start[word[i]]
        print(start)
        start['done'] : 1
    print(words_pedia)
    return answer

solution(['go','gone','guild'])
solution(['abc','def','ghi','jklm'])