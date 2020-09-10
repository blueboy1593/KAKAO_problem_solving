# 1000 ms 단위로 계속 돌리면 당연히 시간초과에 걸린다.
# 구하려고 하는 트래픽의 변화는 문제에서 주어진 lines의 해당하는 것들의 시작과 종료 지점만 생각해주면 된다.

def solution(lines):
    logs = []
    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(':')
        end = (int(h)*60*60 + int(m)*60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end))
    length = len(logs)
    max_ = 1
    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            # 응답시간 max가 3초니깐 그 이상은 break해주는 것.
            if logs[j][1] - logs[i][1] >= 4000:
                break
            # i의 종료 시점에서 시작해서 j의 시작이 1000초 이내일 경우.
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_ = max(max_, cnt)
    return max_

solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
])