from copy import deepcopy

inf = float('inf')
full, stations, problem_station, road_num = list(map(lambda x:int(x),input().split(' ')))
bike_collection = list(map(lambda x:int(x),input().split(' ')))
bike_collection.insert(0,0)
graph = [[inf for i in range(stations+1)]for j in range(stations+1)]
for _ in range(road_num):
    u, v, w = list(map(lambda x:int(x),input().split(' ')))
    graph[u][v] = w
    graph[v][u] = w
u = [0]
data_saver = {}
exp = []
data_saver[0] = {'time': 0, 'road': [[0]]}
for i in range(1,stations+1):
    data_saver[i] = {'time': inf, 'road': None}
for _ in range(stations):
    U = deepcopy(u)
    min_value, next_v = inf, []
    for u in U:
        exp.append(u)
        for v in range(stations + 1):
            w = graph[u][v]
            if w == inf:
                continue
            if v not in exp:
                total_w = w + data_saver[u]['time']
                if total_w == data_saver[v]['time']:
                    data_saver[v]['road'] += list(map(lambda x: x + [v], data_saver[u]['road']))
                if total_w < data_saver[v]['time']:
                    data_saver[v]['time'] = total_w
                    data_saver[v]['road'] = list(map(lambda x: x + [v], data_saver[u]['road']))
                if total_w < min_value:
                    next_v = [v]
                    min_value = total_w
                elif total_w == min_value:
                    next_v.append(v)
    u = next_v



road_list = data_saver[problem_station]['road']
road_to_bike = {}
for road in road_list:
    total = 0
    q = []
    for station in road[1:]:
        q.append(bike_collection[station] - full/2)
    sum_,min_,to = 0, 0,0
    for i in q:
        sum_ += i
        if sum_ < 0:
            if sum_ < min_:
                min_ = sum_
    to = - min_
    back = sum_ + to
    road_to_bike[tuple(road)] = [to,back]
min_to_road = min(road_to_bike.keys(),key=lambda x:road_to_bike[x][0])
print(str(int(road_to_bike[min_to_road][0])),end=' ')
print('->'.join(map(lambda x:str(x),min_to_road)),end=' ')
print(str(int(road_to_bike[min_to_road][1])))