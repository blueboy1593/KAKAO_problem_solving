# 1. divmod를 공부 해야한다. q, r = divmod(n, base)
# 1번의 답: q는 몫, r은 나머지 인듯.!
# 아까 내가 하려던 방법! 몫과 나머지로 계속 뒤에 붙여가면서 가능!

def solution(n, t, m, p):
    answer = ''
    num_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    num_list = []
    tm = t*m
    t_base = 0
    # 비트 연산자를 사용하면 편할까?
    # for t_n in range(t):
    while len(num_list) < tm:
        temp_num = []
        # 솔직히 그냥 간단한 n진법 만들기 문제네
        t_n = t_base
        while True:
            b = t_n % n
            t_n = t_n // n
            temp_num = [num_dict[b]] + temp_num
            # if t_n < n:
            #     temp_num = [num_dict[t_n]] + temp_num
            if t_n == 0:
                break # 훨씬 낫네. 이렇게 바꾸니깐.
        # print('-------------------------')
        # print(temp_num)
        num_list += temp_num
        t_base += 1
    # print(num_list)
    # print(num_list)
    tube_turn = p - 1
    while len(answer) < t:
        answer += num_list[tube_turn]
        tube_turn += m
    # print(answer)
    return answer


solution(16,16,2,2)