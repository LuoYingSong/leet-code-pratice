n = int(input())
stack = []
for _ in range(n):
    operator = input().split(' ')
    try:
        if operator[0] == 'Pop':
            print(stack.pop(-1))
        if operator[0] == 'PeekMedian':
            print(sorted(stack)[(len(stack)+1)//2-1])
        if operator[0] == 'Push':
            stack.append(operator[1])
    except IndexError:
        print('Invalid')