#encoding:gbk
from collections import deque


def sam(num):  # ���ݻ���ʱ��������ʱ��
    a = 8 + num // 60
    b = num % 60
    print('%02d:%02d' % (a, b))


def mapk(num):  # ���ַ����б�ת��Ϊ�����б�
    s = num.copy()
    for i in range(len(num)):
        s[i] = int(num[i])
    return s


num_a = input()
a = list(num_a.split(' '))
num_a = input()
b = list(num_a.split(' '))
num_a = input()
c = list(num_a.split(' '))

a = mapk(a)
b = mapk(b)
c = mapk(c)

max_que = max(c)
time = [0 for i in range(a[2])]
lis = deque([deque([]) for i in range(a[0])])
yell = 1
key = 1
# 8���ϰ�ǰ����źö�(ע����ܴ����˲������������)
for i in range(a[1]):
    if key == 0:
        break
    for j in range(a[0]):
        if yell > a[2]:
            key = 0
            break
        lis[j].append([yell, b[yell - 1]])
        yell += 1
time_cost = 0

# ����ѭ�� ֱ�������Ŷ�
# �ҳ�������ǰ�������Ҫʱ�����Сֵ ��Ҫ���ȵ��� �������µĳ�Ա
# ͬʱע����Сֵ�����Ҳ��ʹ�������е���ǰ��ĳ�Ա��Ҫ��ʱ���С
while True:
    sa = []
    sa_sort = []
    #
    for i in range(a[0]):
        if len(lis[i]) != 0:
            sa.append(lis[i][0][1])
            sa_sort.append(i)
    if len(sa) == 0:
        break;
    ak = min(sa)
    bk = sa.index(ak)
    bk = sa_sort[bk]
    cos = lis[bk].popleft()
    time_cost += cos[1]
    time[cos[0] - 1] = time_cost
    for i in range(a[0]):
        if i != bk and i in sa_sort:
            lis[i][0][1] -= cos[1]
    if yell <= a[2]:
        lis[bk].append([yell, b[yell - 1]])
        yell += 1

for i in c:
    if time[i - 1] - b[i - 1] >= 540:
        print('Sorry')
    else:
        sam(time[i - 1])
