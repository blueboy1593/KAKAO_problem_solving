# 되게 이상하게 짰는데 되기는 되네. 다른 애들꺼 코드 한번 봐야겠다.
def ijin(num, arr, n, i):
    nn = n - 1
    while num > 0:
        if num >= 2**nn:
            num -= 2**nn
            arr[i][n - nn - 1] = '#'
        nn -= 1

def solution(n, arr1, arr2):
    answer = []
    arr_map = [ [0] * n for _ in range(n) ]
    # arr2_map = [ [0] * n for _ in range(n) ]
    for i in range(n):
      ar = arr1[i]
      ijin(ar, arr_map, n, i)
      ar2 = arr2[i]
      ijin(ar2, arr_map, n, i)
    
    # 얘 항상 까묵는다...ㅎ
    for arr in arr_map:
        # answer.append(''.join(map(str, arr))) 일단 버리고
        temp = ''
        for ar in arr:
            if ar == '#':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))