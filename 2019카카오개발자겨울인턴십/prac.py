arr = [1, 3, 6, 10]

stack = []
def permu():
    if len(stack) == 4:
        print(stack)
        return

    for i in range(4):
        if arr[i] not in stack:
            stack.append(arr[i])
            permu()
            stack.pop()

permu()