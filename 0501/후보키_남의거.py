from itertools import chain, combinations

def subset_find(iterable):
    s = list(iterable)
    d = chain.from_iterable(combinations(iterable,r) for r in range(len(iterable) + 1))
    return d

def solution(relation):
    answer_arr = []
    unique_arr = []
    subset_arr = subset_find(list(range(0, len(relation[0]))))

    for subset in subset_arr:
        row_set = set()
        unique = True
        for row in range(len(relation)):
            data = ''
            for column in subset:
                data += relation[row][column] + '.'

            if data in row_set:
                unique = False
                break
            row_set.add(data)

        if unique:
            unique_arr.append(subset)

    unique_arr = sorted(unique_arr, key = lambda x:len(x))

    for subset in unique_arr:
        check = True
        subset = set(subset)
        for j in answer_arr:
            if j.issubset(subset):
                check = False
        if check == True:
            answer_arr.append(subset)
    return len(answer_arr)