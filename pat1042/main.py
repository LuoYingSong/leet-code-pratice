re_use_num = int(input())
index_change_list = list(map(lambda x : int(x)-1,input().split(' ')))
empty_list = [0 for i in range(54)]
init_list = [i for i in range(54)]
for i in range(re_use_num):
    empty_list = [-1 for _ in range(54)]
    for j,num in enumerate(index_change_list):
        empty_list[num] = init_list[j]
    init_list = [new_num if new_num != -1 else old_num for new_num, old_num in zip(empty_list, init_list)]
card_type = ['S','H','C','D','J']
num2card = [type_+str(i) for type_ in card_type for i in range(1,14) ]
for num in init_list[:-1]:
    print(num2card[num],end = ' ')
print(num2card[init_list[-1]])
# print(card_type[(init_list[-1]+1)//13]+str((init_list[-1]+1)%13))