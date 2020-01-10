ret_list = [0 for i in range(3000)]
list1 = list(map(lambda x:float(x),input().split(' ')))[1:]
list2 = list(map(lambda x:float(x),input().split(' ')))[1:]

for i in range(0,len(list1),2):
    for j in range(0,len(list2),2):
        ret_list[int(list1[i]+list2[j])] += list1[i+1]*list2[j+1]
ret_list.reverse()
count = 0
for num in ret_list:
    if num != 0:
        count+=1
print(count,end=' ')
alist = []
for i,num in enumerate(ret_list):
    if num != 0:
        alist.append([2999-i,round(num,1)])

for i,j in enumerate(alist):
    if i == len(alist) - 1:
        print(j[0],j[1],end='')
    else:
        print(j[0], j[1], end=' ')