mark_count,output_count = input().split(' ')
data_list = [[int(data)for data in input().split(' ')] for i in range(int(mark_count))]
output_list = [int(input()) for j in range(int(output_count))]
saver_dict = {}
from functools import reduce
c, m, e, a = [], [], [], []
for data in data_list:
    mark_list = data[1:]
    mark_list.append(reduce(lambda x,y:x+y,mark_list)/3)
    c.append(mark_list[0]),m.append(mark_list[1]),e.append(mark_list[2]),a.append(mark_list[3])
    saver_dict[data[0]] = mark_list
a.sort(reverse=True), c.sort(reverse=True), m.sort(reverse=True), e.sort(reverse=True)
index2lesson={0:'A',1:'C',2:'M',3:'E'}
for id_ in output_list:
    if id_ not in saver_dict.keys():
        print('N/A')
        continue
    mark_list = saver_dict[id_]
    rank_list = [a.index(mark_list[3]),c.index(mark_list[0]),m.index(mark_list[1]),e.index(mark_list[2])]
    rank = min(rank_list)
    lesson = index2lesson[rank_list.index(rank)]
    print(rank+1,lesson)


