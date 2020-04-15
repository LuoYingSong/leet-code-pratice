length, spend_money = list(map(lambda x: int(x), input().split(' ')))
demon_list = list(map(lambda x: int(x), input().split(' ')))
sum_list = [0]
summary = 0
for num in demon_list:
    summary += num
    sum_list.append(summary)
j, min_num, flag = 0, float('inf'), 1
saver = []
for i in range(1, length + 1):
    while j <= length and sum_list[j] - sum_list[i - 1] < spend_money:
        j += 1
    if j == length+1:
        break
    if sum_list[j] - sum_list[i - 1] == spend_money:
        flag = 0
        print(str(i)+'-'+str(j))
        min_num = -float('inf')
        continue
    if sum_list[j] - sum_list[i - 1] < min_num:
        # print(sum_list[j] , sum_list[i - 1] , min_num)
        saver = [[str(i), str(j)]]
        min_num = sum_list[j] - sum_list[i - 1]
    elif sum_list[j] - sum_list[i - 1] == min_num:
        saver.append([str(i), str(j)])
if flag:
    for index_list in saver:
        print('-'.join(index_list))