inf = float('inf')
n = int(input())
graph = [[inf for i in range(n)] for j in range(n)]
for i in range(n - 1):
    u, v = list(map(lambda x: int(x), input().split(' ')))
    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1


total = dict(zip(range(n),[1 for i in range(n)]))
line = dict(zip(range(n),[set() for i in range(n)]))

def dfs(point,start,exp):
    line[start].add(point)
    exp = list(exp)
    exp.append(point)
    flag = 0
    for v in range(n):
        if graph[point][v] == 1 and v not in exp:
            flag = 1
            dfs(v,start,tuple(exp))
    if not flag:
        total[start] = max(len(exp),total[start])
        return exp

for i in range(n):
    dfs(i,i,())
connected_components_length = len(set(map(lambda x:tuple(x),line.values())))
if connected_components_length== 1:
    result = sorted([k+1 for k,v in total.items() if v == max(total.values())])
    print('\n'.join(map(lambda x : str(x),result)))
else:
    print('Error: {} components'.format(connected_components_length))
