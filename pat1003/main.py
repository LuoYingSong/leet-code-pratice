# class City(object):
#
#     def __init__(self, index, rescue, distance=sys.maxsize):
#         self.index = index
#         self.rescue = rescue
#         self.distance = distance
#         self.prev = []
#
#     def __lt__(self, other):
#         return self.distance < other.distance

def main():
    ptr_num, line_num, start_ptr, end_ptr = list(map(lambda x:int(x),input().split(' ')))
    people = list(map(lambda x:int(x),input().split(' ')))
    dist_list = [[-1 for j in range(ptr_num)] for i in range(int(ptr_num))]
    used = [False for _ in range(ptr_num)]
    for i in range(line_num):
        str4=list(map(lambda x:int(x),input().split(' ')))
        dist_list[str4[0]][str4[1]] = str4[2]
        dist_list[str4[1]][str4[0]] = str4[2]
    min_dist = [1000 for i in range(ptr_num)]
    min_dist[start_ptr] = 0
    people_list = [0 for i in range(ptr_num)]
    people_list[start_ptr] = people[start_ptr]
    line_num = [0 for i in range(ptr_num)]
    line_num[start_ptr] = 1
    while True:
        v = -1
        for u in range(ptr_num):
            if not used[u] and (v == -1 or min_dist[u] < min_dist[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(ptr_num):
            if dist_list[u][v] != -1 :
                old_dist = min_dist[u]
                new_dist = min_dist[v] + dist_list[u][v]
                if old_dist > new_dist:
                    min_dist[u] = new_dist
                    people_list[u] = people_list[v] + people[u]
                    line_num[u] = line_num[v]
                if old_dist == new_dist:
                    line_num[u] += line_num[v]
                    people_list[u] = max(people_list[v] + people[u],people_list[u])
    print(line_num[end_ptr],people_list[end_ptr])

if __name__ == '__main__':

    main()