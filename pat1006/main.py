count = int(input())
start_list = []
end_list = []
id_list = []
for i in range(count):
    id_, start, end = input().split(' ')
    start_list.append(start)
    if start>end:
        continue
    end_list.append(end)
    id_list.append(id_)
start_index = start_list.index(min(start_list))
end_index = end_list.index(max(end_list))
# if start_index == end_index:
#     print(id_list[start_index],end='')
# else:
print(id_list[start_index],id_list[end_index],end='')