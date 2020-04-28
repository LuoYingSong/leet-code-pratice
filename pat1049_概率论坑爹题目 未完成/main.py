num_str = input()
length = len(num_str)
count = 0
for i, num in enumerate(num_str):
    num = int(num)
    left_num = int(num_str[:i] if num_str[:i] != '' else 0)
    right_num = int(num_str[i + 1:]if num_str[i + 1:] != '' else 0)
    if num == 0:
        count += left_num * 10 ** (length - i - 1)
    elif num == 1:
        count += left_num * 10 ** (length - i - 1) + right_num + 1
    else:
        count += (left_num + 1) * 10 ** (length - i - 1)
print(count)