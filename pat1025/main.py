n = int(input())
total = {} #mark:[id,class]
class_num = 0
counter = 0
for i in range(n):
    m = int(input())
    for j in range(m):
        id_, mark = list(map(lambda x: int(x), input().split(' ')))
        if mark not in total.keys():
            total[mark] = {id_:i}
        else:
            total[mark][id_] = i
        counter += 1
    class_num = i

count_list = [1 for i in range(class_num+1)]
count = 1
print(counter)
for mark in sorted(total.keys(),reverse=True):
    length = len(total[mark])
    length_list = [0 for i in range(class_num+1)]
    for id_ in sorted(total[mark].keys()):
        print(id_,end=' ')
        print(count,end=' ')
        class_index = total[mark][id_]
        print(class_index+1,end=' ')
        print(count_list[class_index])
        length_list[class_index] += 1
    for i in range(class_num+1):
        count_list[i] += length_list[i]
    count += length