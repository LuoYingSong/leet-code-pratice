start1, start2, line = input().split(' ')
pre2next = []
pre2next_dict = {}
flag = 1
total = -1
for i in range(int(line)):
    start, _, end = input().split(' ')
    if flag and end not in pre2next:
        pre2next.append(end)
    else:
        flag = 0
        total = end
    pre2next_dict[start] = end
if total == -1:
    print(-1)
else:
    saver = []
    for start in [start1,start2]:
        pre = start
        while pre != '-1':
            next_addr = pre2next[pre]
            if next_addr == total:
                saver.append(1)
                break
            pre = next_addr
    if len(saver) != 2:
        print(-1)
    else:pre
