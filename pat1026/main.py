def str2second(time_):
    time_list = list(map(lambda x: int(x), time_.split(':')))
    return time_list[0] * 60 + time_list[1] + time_list[2] / 60


n = int(input())

time = {}
for i in range(n):
    arrive_time, play_time, is_vip = input().strip().split(' ')
    second = str2second(arrive_time)
    if 21*60>=second:
        time[second] = [arrive_time, min(120,int(play_time)), int(is_vip)]
total_table, vip_table = list(map(lambda x: int(x), input().strip().split(' ')))
vip_table_list = list(map(lambda x: int(x)-1, input().strip().split(' ')))
time_list = sorted(time.keys())
table_status = [8*60 for i in range(total_table)]
total_queue = []
saver = {}  # {'begin_time':'end_time'}
vip_queue = []
server_people = [0 for i in range(total_table)]



def find_table(begin_time,now_time,is_vip):
    if is_vip:
        table_list = vip_table_list
    else:
        table_list = range(len(table_status))
    if begin_time >= 21*60:
        return -1,-1
    for j in table_list:
        if table_status[j] <= begin_time:
            return j,0
    min_over_time = 999999999
    index = -1
    for j in table_list:
        if table_status[j] < min_over_time:
            min_over_time = table_status[j]
            index = j

    if min_over_time >= 21*60:
        return -1,-1
    if is_vip:
        _,min_over_time_not_vip = find_table(begin_time,now_time,0)
        if min_over_time_not_vip < min_over_time-begin_time:
            return None,-1
    if min(table_status) - now_time < 0:
        return index,min_over_time-begin_time
    return None,-1

def int2str(time_):
    hour = time_ // 60
    minute = int(time_ % 60)
    second = 60 * (time_% 60 - int(time_ % 60))
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(int(hour),int(minute),int(second))

i = 0
flag = 1
while (total_queue or i < len(time_list)) and flag:
    # print(total_queue , time_list)
    if i >= len(time_list):
        new_time = 21*60
    else:
        new_time = time_list[i]
    while vip_queue:
        user = vip_queue[0]
        # if user[0] == '15:26:58':
        #     print(1)
        table_index,waitting_time = find_table(str2second(user[0]),new_time,1)
        if table_index is None:
            break
        elif table_index == -1:
            flag = 0
            del vip_queue[0]
            total_queue.remove(user)
            break
        else:
            print('{} {} {}'.format(user[0],int2str(str2second(user[0])+waitting_time),int(waitting_time+0.5)))
            server_people[table_index] += 1
            del vip_queue[0]
        end_time = str2second(user[0]) + user[1] + waitting_time
        table_status[table_index] = end_time
        total_queue.remove(user)
    while total_queue:
        user = total_queue[0]
        table_index,waitting_time = find_table(str2second(user[0]), new_time, 0)
        end_time = str2second(user[0]) + user[1]+ waitting_time
        if table_index is None:
            break
        elif table_index == -1:
            flag = 0
            break
        else:
            print('{} {} {}'.format(user[0], int2str(str2second(user[0]) + waitting_time), int(waitting_time + 0.5)))
            server_people[table_index] += 1
            del total_queue[0]
            if user[2]:
                vip_queue.remove(user)
        table_status[table_index] = end_time
    if i < len(time_list):
        if time[new_time][2]:
            vip_queue.append(time[new_time])
        total_queue.append(time[new_time])
    i += 1

print(' '.join(map(lambda x:str(x),server_people)))