from functools import cmp_to_key
n, m = list(map(int, input().split(' ')))
saver = []
for i in range(n):
    name, age, money = input().split(' ')
    saver.append([name, int(age), int(money)])
key_list = []
start2line = {}
def cmp(list1,list2):
    if list1[2]>list2[2]:
        return 1
    if list1[2]<list2[2]:
        return -1
    if list1[1]>list2[1]:
        return -1
    if list1[1]<list2[1]:
        return 1
    if list1[0]>list2[0]:
        return -1
    else:
        return 1
for i in range(m):
    line, start, end = list(map(int,input().split(' ')))
    datas = []
    for data in saver:
        if end>=data[1]>=start:
            datas.append(data)
    print('Case #{}:'.format(i+1))
    if len(datas) == 0:
        print('None')
    else:
        datas = sorted(datas,key=cmp_to_key(cmp),reverse=True)
        for data in datas[:line]:
            print(' '.join(map(str,data)))