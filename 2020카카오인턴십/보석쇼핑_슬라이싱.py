def solution(gems):
    answer = []
    set_gems = set(gems)
    # for i in range(len(gems)):
    #     for j in range(1, len(gems) - i + 1):
    #         print(gems[i:i + j])
    j = 1
    while j < len(gems) + 1:    
        for i in range(len(gems) + 1 - j):
            buy_gems = gems[i:i + j]
            if set_gems == set(buy_gems):
                return [i + 1, i + j]
        j += 1


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])