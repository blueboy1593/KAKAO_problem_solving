def remove_sharp(m):
    new_m = ''
    for i in range(len(m) - 1):
        if m[i + 1] == '#':
            new_m += m[i].lower()
        elif m[i] == '#':
            continue
        else:
            new_m += m[i]
    new_m += m[-1]
    return new_m

def solution(m, musicinfos):
    m = remove_sharp(m)
    answer = ''
    hubo_list = []
    for musicin in musicinfos:
        info_list = musicin.split(',')
        # print(info_list)
        start_h, start_m = info_list[0].split(':')
        end_h, end_m = info_list[1].split(':')
        time_h = int(end_h) - int(start_h)
        time_m = int(end_m) - int(start_m)
        total_time = 60*time_h + time_m
        # print(total_time)
        music = info_list[2]
        melody = info_list[3]
        melody = remove_sharp(melody)

        melody_string = ''
        melody_leng = len(melody)
        index = 0
        for _ in range(total_time):
            melody_string += melody[index]
            index += 1
            if index == melody_leng:
                index = 0
        # print(melody_string)
        if m in melody_string:
            hubo_list.append((total_time, music))
    # print(hubo_list)
    hubo_list.sort(reverse=True)
    if hubo_list != []:
        answer = hubo_list[0][1]
    else:
        answer = "`(None)`"
    return answer


solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF'])