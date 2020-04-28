num, group = list(map(int, input().split(' ')))
rank_list = list(map(int, input().split(' ')))
groups = list(map(int, input().split(' ')))
rank_dict = dict(zip(range(len(rank_list)),rank_list))
rank_dict2 = rank_dict.copy()
people_in_group = []
data_saver = {}
total_del_list = []
count = 1
while len(rank_dict.keys())!=1:
    # print(rank_dict)
    del_list = []
    for i,people in enumerate(groups):
        if people not in rank_dict.keys():
            pass
        else:
            people_in_group.append(people)
        if len(people_in_group) == group or i == len(groups)-1:
            try:
                max_people = max(people_in_group,key=lambda x:rank_dict2[x])
                for this_turn_people in people_in_group:
                    if this_turn_people != max_people:
                        del rank_dict[this_turn_people]
                        del_list.append(this_turn_people)
                people_in_group.clear()
            except Exception:
                pass
    total_del_list.append(del_list)
    count += 1
else:
    total_del_list.append(list(rank_dict.keys()))
total = 1
for i,del_list in enumerate(reversed(total_del_list)):
    for people in del_list:
        data_saver[people] = total
    total += len(del_list)
for i in range(num-1):
    print(data_saver[i],end=' ')
print(data_saver[num-1])
