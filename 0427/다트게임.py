def solution(dartResult):
    answer = 0
    score_list = [0] * 4
    stack_list = []
    # stack = ['', '', '']
    num = ''
    for i in range(len(dartResult)):
        if dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T":
            if i != len(dartResult) - 1:
                if dartResult[i + 1] == "*" or dartResult[i + 1] == "#":
                    stack_list.append([num, dartResult[i], dartResult[i + 1]])
                else:
                    stack_list.append([num, dartResult[i], 0])
                num = ''
            else:
                # 마지막이니까 num='' 초기화 필요 X
                stack_list.append([num, dartResult[i], 0])
        elif dartResult[i] == "*" or dartResult[i] == "#":
            pass
        else:
            num += dartResult[i]
    # print(stack_list)
    for j in range(3):
        stack = stack_list[j]
        a, b, c = stack
        a = int(a)
        jpl = j + 1
        if b == 'S':
            score_list[jpl] = a
        elif b == 'D':
            score_list[jpl] = a**2
        else:
            score_list[jpl] = a**3
        if c != 0:
            if c == "*":
                score_list[j] *= 2
                score_list[jpl] *= 2
            elif c == "#":
                # score_list[j] = -score_list[j] 아차상은 해당 점수만!
                score_list[jpl] = -score_list[jpl]
    # print(score_list)
    answer = sum(score_list)
    return answer

solution("1D2S#10S")