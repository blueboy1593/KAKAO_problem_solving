def solution(record):
    answer = []
    pre_answer = []
    idnick_dict = dict()

    for rec in record:
        rec = rec.split(' ')
        print(rec)
        if rec[0] == "Enter":
            pre_answer.append([rec[1], 'E'])
            idnick_dict[rec[1]] = rec[2]
        elif rec[0] == "Leave":
            pre_answer.append([rec[1], "L"])
        else:
            idnick_dict[rec[1]] = rec[2]

    for pre in pre_answer:
        uuid, state = pre
        if state == "E":
            nick = idnick_dict[uuid]
            sentence = nick + '님이 들어왔습니다.'
            answer.append(sentence)
        else:
            nick = idnick_dict[uuid]
            sentence = nick + '님이 나갔습니다.'
            answer.append(sentence)
    # print(answer)
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])