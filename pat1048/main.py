_, money = list(map(lambda x: int(x), input().split(' ')))
money_list2 = list(map(lambda x: int(x), input().split(' ')))
money_list = sorted(money_list2)
flag = 0
saver = []


def find_num(num_list, num):
    if len(num_list) == 0 or (len(num_list) == 1 and num_list[len(num_list) // 2] != num):
        return False
    if num_list[len(num_list) // 2] == num:
        return True
    elif num_list[len(num_list) // 2] < num:
        return find_num(num_list[len(num_list) // 2:], num)
    elif num_list[len(num_list) // 2] > num:
        return find_num(num_list[:len(num_list) // 2], num)

for i,coin in enumerate(money_list):
    if not find_num(money_list[i+1:], money - coin):
        pass
    else:
        flag = 1
        saver.append(min(coin,money-coin))
if not flag:
    print('No Solution')
else:
    coin = min(saver)
    print(coin,money-coin)