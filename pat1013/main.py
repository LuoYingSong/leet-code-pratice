citys_num, lines_num, _ = list(map(lambda x: int(x), input().split(' ')))

city_graph = [[0 for i in range(citys_num)] for j in range(citys_num)]

for i in range(lines_num):
    line = list(map(lambda x: int(x), input().split(' ')))
    city_graph[line[0] - 1][line[1] - 1] = 1
    city_graph[line[1] - 1][line[0] - 1] = 1
output_list = list(map(lambda x: int(x), input().split(' ')))

from functools import lru_cache


cache = []
@lru_cache()
def find_city(city,destory_city):
    print(1)
    if city not in cache:
        cache.append(city)
    else:
        return None
    can_line_city = set()
    can_line_city.add(city)
    for i, line in enumerate(city_graph[city]):
        if line == 1 and i != destory_city:
            # print(i)
            can_line_city.add(i)
    # total_city = set()
    for city in can_line_city:
        add_set = find_city(city,destory_city)
        # print(add_set)
        if add_set is not None:
            can_line_city = can_line_city | add_set
    return can_line_city


# from copy import deepcopy
for output in output_list:
    cache = []
    add_num = 0
    destory_city = output - 1
    start_city = 0 if destory_city != 0 else 1
    can_line_city = set()
    total_city = set(range(citys_num))
    total_city.remove(destory_city)
    if len(total_city) == 0:
        print(0)
        continue
    # print(total_city)
    while True:
        a = find_city(start_city,destory_city)
        can_line_city = can_line_city | a
        # print(start_city,a,can_line_city)
        if len(can_line_city) < citys_num-1:
            add_num+=1
            start_city = (total_city - can_line_city).pop()
        else:
            break
    print(add_num)
