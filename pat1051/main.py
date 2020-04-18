full, push_max, n = list(map(int, input().split(' ')))


# def is_full(num_list):
#     stack = []
#     for num in num_list:
#         if not stack:
#             stack.append(num)
#         else:
#             while stack and num > stack[-1]:
#                 stack.pop()
#             stack.append(num)
#         if len(stack) > full:
#             return False
#     return True

def is_useful(num_list):
    j = 0
    stack = []
    for i in range(1,push_max+1):
        stack.append(i)
        if len(stack) > full:
            return False
        while stack and stack[-1] == num_list[j]:
            stack.pop()
            j += 1
    if j == push_max:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(n):
        inputs = (list(map(int, input().split(' '))))
        if is_useful(inputs):
            print('YES')
        else:
            print('NO')