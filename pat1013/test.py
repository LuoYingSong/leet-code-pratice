from functools import lru_cache


city_graph=[[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0]]




# @lru_cache()
cache = []
def find_city(city,destory_city):
    if city not in cache:
        cache.append(city)
    else:
        return None
    can_line_city = set()
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

if __name__ == '__main__':
    print(find_city(2,destory_city=1))