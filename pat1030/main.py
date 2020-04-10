inf = float('inf')
station, line, start, end = list(map(lambda x:int(x),input().split(' ')))
graph = [[inf for i in range(station)] for j in range(station)]
cost = [[inf for _ in range(station)] for _ in range(station)]
for i in range(line):
    u,v,w,c = list(map(lambda x: int(x), input().split(' ')))
    graph[u][v] = w
    graph[v][u] = w
    cost[u][v] = c
    cost[v][u] = c

U = [start]
exp = [start]
weight = [inf for _ in range(station)]
weight[0] = 0
line_list = [[] for _ in range(station)]
line_list[0].append([0])
while True:
    if not U:
        break
    next_U = []
    min_value = inf
    for u in U:
        exp.append(u)
        for v in range(station):
            w = graph[u][v]
            if w != inf and v not in exp:
                if min_value > w + weight[u]:
                    next_U = [v]
                    weight[v] = w + weight[u]
                    print(line_list)
                    pre_line_list = list(map(lambda x:x+[v],line_list[u]))
                    line_list[v] = pre_line_list
                elif min_value == w:
                    next_U.append(v)
                    pre_line_list = list(map(lambda x: x + [v], line_list[u]))
                    line_list[v] += pre_line_list
    U = next_U