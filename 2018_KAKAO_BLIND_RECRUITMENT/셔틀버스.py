def solution(n, t, m, timetable):
    answer = ''
    timeinsecond = [0] * 1440
    shuttle = [ [0] * m for _ in range(n) ] # 아 이거 맞네 ㅡ.ㅡ
    # print(shuttle)
    
    timetable_ins = []
    for crew in timetable:
        ######################################## 시간형식 바꾸는거 다른사람꺼 꼭 참조해보자.
        h, mm = crew.split(':')
        crew_time = int(h)*60 + int(mm)
        timetable_ins.append(crew_time)
    timetable_ins.sort()
    # print(timetable_ins)
    for crew_t in timetable_ins:
        boarding = False
        if 0 < crew_t <= 540: # 첫차에 탈 수 있냥
            for i in range(m):
                if shuttle[0][i] == 0:
                    shuttle[0][i] = crew_t # 일단 이 버스 태운다
                    boarding = True
                    break
        if boarding == True:
            continue
        for j in range(n - 1):
            ss = 540 + j*t
            ee = 540 + (j + 1)*t
            # if ss < crew_t <= ee:
            if crew_t <= ee: # 각각 다음 호차들에 탈 수 있냥// 최소 제한은 필요 없는듯 하다.
                for i in range(m):
                    if shuttle[j + 1][i] == 0:
                        shuttle[j + 1][i] = crew_t
                        boarding = True
                        break
            if boarding == True:
                break
        # if boarding == False:
        #     break 이건 나중에 시도해보자.
    # print(shuttle) #일단은 태우는데 성공은 했어...

    # 마지막 단계: 뒤에서부터 검증 X 뒤에서 하나만 검증하면 됨!
    if shuttle[n - 1][m - 1] == 0:
        answer = 540 + (n - 1)*t
    else:
        answer = shuttle[n - 1][m - 1] - 1
    hh, mmm = divmod(answer, 60)
    #####################################################남의 코드 보자. 시간대로 바꾸는 함수.
    if hh < 10:
        hh = '0' + str(hh)
    else:
        hh = str(hh)
    if mmm < 10:
        mmm = '0' + str(mmm)
    else:
        mmm = str(mmm)
    
    answer = hh + ':' + mmm
    # print(answer)
    return answer

solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03'])
solution(2, 10, 2, ['09:10', '09:09', '08:00'])