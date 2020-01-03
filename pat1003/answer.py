import sys
import queue


class City(object):

    def __init__(self, index, rescue, distance=sys.maxsize):
        self.index = index
        self.rescue = rescue
        self.distance = distance
        self.prev = []

    def __lt__(self, other):
        return self.distance < other.distance


def main():
    city_num, roads, src, des = [int(_) for _ in input().split()]
    city_rescue = [int(_) for _ in input().split()]

    cities = [City(i, city_rescue[i]) for i in range(city_num)]
    cities[src].distance = 0

    city_map = list()
    for i in range(city_num):
        city_map.append([sys.maxsize if i != j else 0 for j in range(city_num)])

    for i in range(roads):
        c1, c2, weight = [int(_) for _ in input().split()]
        city_map[c1][c2] = weight
        city_map[c2][c1] = weight

    mark = [False for _ in range(city_num)]
    pq = queue.PriorityQueue()
    pq.put(cities[src])
    for i in range(city_num):
        if not pq.empty():
            city = pq.get()
            mark[city.index] = True

            for c2, weight in enumerate(city_map[city.index]):
                if weight != sys.maxsize and not mark[c2]:
                    new_weight = city.distance + weight

                    if new_weight == cities[c2].distance:
                        cities[c2].prev.append(city.index)
                        continue

                    if new_weight < cities[c2].distance:
                        cities[c2].distance = new_weight
                        cities[c2].prev = [city.index]
                        if cities[c2].index not in [q.index for q in pq.queue]:
                            pq.put(cities[c2])
        else:
            for i in range(city_num):
                if not mark[i]:
                    pq.put(cities[i])
                    break

    road_num = 0
    rescue_num = 0

    def recurisive(city_obj, res_num):
        nonlocal road_num, rescue_num

        if city_obj.index == src:
            road_num += 1
            if res_num + city_obj.rescue > rescue_num:
                rescue_num = res_num + city_obj.rescue
        elif city_obj.prev:
            for c_index in city_obj.prev:
                recurisive(cities[c_index], res_num + city_obj.rescue)

    recurisive(cities[des], 0)
    print('{} {}'.format(road_num, rescue_num), end='')


if __name__ == '__main__':
    main()