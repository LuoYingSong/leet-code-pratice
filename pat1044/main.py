length, spend_money = list(map(lambda x: int(x), input().split(' ')))
demon_list = list(map(lambda x: int(x), input().split(' ')))
demon_list = demon_list
i, j = 0, 0
min_num = +float('inf')
flag = 0
saver = []
sum_num = 0
while True:
    if sum_num < spend_money:
        sum_num += demon_list[j]
        j += 1
    elif sum_num > spend_money:
        if sum_num < min_num:
            min_num = sum_num
            saver = [[i + 1, j]]
        elif sum_num == min_num:
            saver.append([i + 1, j])
        sum_num -= demon_list[i]
        i += 1
    else:
        print(str(i + 1) + '-' + str(j))
        sum_num -= demon_list[i]
        i += 1
        flag = 1
    if i == length:
        break
    if j == length:
        while True:
            sum_num -= demon_list[i]
            i += 1
            if sum_num>spend_money:
                if sum_num < min_num:
                    min_num = sum_num
                    saver = [[i + 1, j]]
                elif sum_num == min_num:
                    saver.append([i + 1, j])
            else:
                break
        break
if not flag:
    for index_list in saver:
        print('-'.join(map(str, index_list)))
