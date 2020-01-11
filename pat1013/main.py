citys_num, lines_num, _= list(map(lambda x:int(x),input().split(' ')))

city_graph = [[0 for i in range(citys_num)] for j in range(citys_num)]

for i in range(lines_num):
    line = list(map(lambda x:int(x),input().split(' ')))
    city_graph[line[0]-1][line[1]-1] = 1
    city_graph[line[1]-1][line[0]-1] = 1
output_list = list(map(lambda x:int(x),input().split(' ')))


def find_line(graph,start,used_list):
    for city,road in enumerate(graph[start]):
        if city not in used_list and road == 1:
            used_list.append(city)
            used_list = find_line(graph,city,used_list)
    return used_list


from copy import deepcopy

for city in output_list:
    city = city - 1
    graph = deepcopy(city_graph)
    for i in range(len(graph)):
        graph[i][city] = 0
        graph[city][i] = 0
    total = set()
    for start_city in output_list:
        if (start_city - 1) != city:
            total = total | set(find_line(graph,start_city -1 ,used_list=[]))
    if citys_num - 1 == len(total):
        print(0)
    else:
        print(citys_num - 1 - len(total)-1)