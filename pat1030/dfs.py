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

total = []
def dfs(start,end,exp):
    exp = list(exp)
    exp.append(start)
    exp = tuple(exp)
    if start == end:
        total.append(exp)
        return exp
    for i in range(station):
        if graph[start][i] != inf and i not in exp:
            dfs(i,end,exp)

dfs(start,end,[])
min_line = None
min_value = inf
min_c = inf
for line in total:
    total_w = 0
    total_c = 0
    for pre,next in zip(line[:-1],line[1:]):
        total_w += graph[pre][next]
        total_c += cost[pre][next]
    if (total_w<min_value) or (total_w == min_value and total_c < min_c):
        min_value = total_w
        min_line = line
        min_c = total_c
# print(min_c,min_value,min_line)
print(' '.join(map(lambda x:str(x),min_line)),end=' ')
print(min_value,end=' ')
print(min_c)