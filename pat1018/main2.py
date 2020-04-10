from copy import deepcopy
#use dfs
inf = float('inf')
full, stations, problem_station, road_num = list(map(lambda x:int(x),input().split(' ')))
bike_collection = list(map(lambda x:int(x),input().split(' ')))
bike_collection.insert(0,0)
graph = [[inf for i in range(stations+1)]for j in range(stations+1)]
for _ in range(road_num):
    u, v, w = list(map(lambda x:int(x),input().split(' ')))
    graph[u][v] = w
    graph[v][u] = w
total_list = []
def dfs(u,value,exp):
    exp = list(exp)
    exp.append(u)
    exp = tuple(exp)
    for v in range(stations+1):
        if graph[u][v] != inf and v not in exp:
            if v == problem_station:
                total_list.append([list(exp)+[v],value+graph[u][v]])
                return
            else:
                dfs(v,value+graph[u][v],exp)
dfs(0,0,[])
roads = []
min_ = inf
for road,weight in total_list:
    if min_ > weight:
        min_ = weight
        roads = [road]
    elif min_ == weight:
        roads.append(road)
road_to_bike = {}
for road in roads:
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