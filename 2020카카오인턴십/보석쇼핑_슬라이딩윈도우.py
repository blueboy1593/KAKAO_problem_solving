from collections import defaultdict

def solution(gems):
    answer = [0, 0]
    candidates = []
    sta, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    
    while True:
        kind = len(gems_dict)
        if sta == gems_len:
            break
        if kind == gem_kind:
            candidates.append((sta, end))
            gems_dict[gems[sta]] -= 1
            if gems_dict[gems[sta]] == 0:
                del gems_dict[gems[sta]]
            sta += 1
            continue
        if end == gems_len:
            break
        if kind != gem_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue

    length = float('inf')
    for s, e in candidates:
        if length > e-s:
            length = e-s
            answer[0] = s + 1
            answer[1] = e
    return answer


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])