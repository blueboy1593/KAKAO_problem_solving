def solution(record):
    answer = []
    pre_answer = []
    idnick_dict = dict()

    for rec in record:
        # 오예! 이 로직 성공!
        if rec[0] == "E":
            rec2 = rec.lstrip('Enter ')
            uid = ''
            for i in range(len(rec2)):
                if rec2[i] ==' ':
                    break
                else:
                    uid += rec2[i]
            nickname = rec2.lstrip(uid + ' ')
            # id와 E 넣어주기!
            pre_answer.append([uid, 'E'])
            # if not uid in idnick_dict:
            #     idnick_dict[uid] = nickname
            # else: # 이거 일부러 해주는거야
            idnick_dict[uid] = nickname
        elif rec[0] == "L":
            uid = rec.lstrip('Leave ')
            pre_answer.append([uid, "L"])
        elif rec[0] == "C":
            rec2 = rec.lstrip('Change ')
            uid = ''
            for i in range(len(rec2)):
                if rec2[i] ==' ':
                    break
                else:
                    uid += rec2[i]
            nickname = rec2.lstrip(uid + ' ')
            idnick_dict[uid] = nickname
    # print(pre_answer)
    # print(idnick_dict)
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