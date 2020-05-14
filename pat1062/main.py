from functools import cmp_to_key

def cmp(a,b):
    if sum([a[1],a[2]]) > sum([b[1],b[2]]):
        return 1
    elif sum([a[1],a[2]]) < sum([b[1],b[2]]):
        return -1
    else:
        if a[1]>b[1]:
            return 1
        elif a[1]<b[1]:
            return -1
        else:
            if a[0]>b[0]:
                return -1
            else:
                return 1


n, low, high = [int(i) for i in input().split(' ')]
saver = {'sage': [], 'nobleman': [], 'fool_men': [], 'other': []}
for _ in range(n):
    id_, virtue, talent = list(map(int, input().split()))
    if virtue >= low and talent >= low:
        if virtue >= high and talent >= high:
            saver['sage'].append([id_, virtue, talent])
        elif talent < high and virtue >= high:
            saver['nobleman'].append([id_, virtue, talent])
        elif virtue < high and talent < high and virtue >= talent:
            saver['fool_men'].append([id_, virtue, talent])
        else:
            saver['other'].append([id_, virtue, talent])
ret_data = []
for title in ['sage', 'nobleman', 'fool_men', 'other']:
    ret_data += sorted(saver[title], key=cmp_to_key(cmp),reverse=True)
print(len(ret_data))
for data in ret_data:
    print('{} {} {}'.format(data[0],data[1],data[2]))
