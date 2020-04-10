total = 0
inputs = []
for i in range(2):
    length, *args = list(map(lambda x: int(x), input().split(' ')))
    inputs.append(args)
    total += length
inputs = sorted(inputs[0] + inputs[1])
# print(inputs.index(-1339),total // 2 - 1)
# print(total)4 11 12 13 14
# 5 9 10 15 16 17
if total % 2:
    print(inputs[total // 2])
else:
    print(inputs[total // 2 - 1])