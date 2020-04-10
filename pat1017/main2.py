import sys
def time2minute(date):
    date_list = date.split(':')
    second = float(date_list[2])/60 + int(date_list[1])  + int(date_list[0]) * 60
    return second


data_num, queue_length = list(map(lambda x:int(x),input().split(' ')))
time2wait_time = {}
for i in range(data_num):
    time, wait_time = input().split(' ')
    time2wait_time[time2minute(time)] = float(wait_time)
count = 0
sum_wait_time = 0
queue_list = [[] for i in range(queue_length)]
old_time = 480
for time in sorted(time2wait_time.keys()):
    if time > 17 * 60:
        break
    else:
        count+=1
    if time < 480:
        min_time = sys.maxsize
        for i,queue in enumerate(queue_list):
            if sum(queue) < min_time:
                min_time = sum(queue)
                min_index = i
        # print(((480-time)+min_time))
        sum_wait_time += ((480-time)+min_time)
        queue_list[min_index].append(time2wait_time[time])
        queue = queue_list[min_index]
        queue_list[min_index] = [queue[0]] + sorted(queue[1:])
    else:
        pass_time = time - old_time
        for k,queue in enumerate(queue_list):
            del_list = []
            for j,people in enumerate(queue):
                if people - pass_time <= 0:
                    del_list.append(j)
                    pass_time = pass_time - people
                else:
                    queue[j] = people - pass_time
                    break
            queue = [wait_time for wait_index,wait_time in enumerate(queue) if wait_index not in del_list]
        min_time = sys.maxsize
        for i,queue in enumerate(queue_list):
            if sum(queue) < min_time:
                min_time = sum(queue)
                min_index = i
        # print(min_time)
        sum_wait_time += min_time
        queue_list[min_index].append(time2wait_time[time])
        queue = queue_list[min_index]
        queue_list[min_index] = [queue[0]] + sorted(queue[1:])
        old_time = time
print('{:.1f}'.format(sum_wait_time / (count if count != 0 else 1)))