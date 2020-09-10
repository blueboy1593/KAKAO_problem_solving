def solution(lines):
    answer = 0
    time_arr = [0] * 86400000

    for line in lines:
        new_line = line.lstrip('2016-09-15')
        new_line = new_line.split(' ')
        a, b, c = new_line
        d = b.split(':')
        e = c.rstrip('s')
        f = int(float(e) * 1000)
        h, m, s = d
        s = int(float(s) * 1000)
        m = int(m) * 1000 * 60
        h = int(h) * 1000 * 60 * 60
        base = h + m + s
        for t in range(f):
            time_arr[base + t] += 1
    
    for i in range(1000):
        basic += 

    for i in range(86400000 - 1000):


    return answer


# solution([
# '2016-09-15 01:00:04.001 2.0s',
# '2016-09-15 01:00:07.000 2s'
# ])
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

