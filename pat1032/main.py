has_view = {}
start1, start2, line = input().split(' ')
pre2next = {}
flag = 1
for i in range(int(line)):
    start, _, end = input().split(' ')
    pre2next[start] = end
    has_view[start] = False
    has_view[end] = False
pre = start1
while pre != '-1':
    has_view[pre] = True
    next_addr = pre2next[pre]
    pre = next_addr
pre = start2
while pre != '-1':
    if has_view[pre]:
        print(pre)
        flag=0
        break
    next_addr = pre2next[pre]
    pre = next_addr
if flag:
    print(-1)