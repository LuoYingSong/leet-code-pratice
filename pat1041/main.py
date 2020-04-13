num_list = list(map(int, input().split(' ')))[1:]
adict = dict(zip(set(num_list),[0 for _ in range(len(set(num_list)))]))
for num in num_list:
    adict[num]+=1
for num in num_list:
    if adict[num] == 1:
        print(num)
        exit()
print('None')