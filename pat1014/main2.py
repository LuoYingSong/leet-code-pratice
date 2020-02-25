#encoding:gbk
from copy import deepcopy
import sys


def sam(num):
    a = (8 + num // 60 )% 24
    b = num % 60
    print('%02d:%02d' % (a, b))

now_time = 0
queue_num, queue_length, _,_ = list(map(lambda x: int(x), input().split(' ')))
people_waitting = list(map(lambda x: int(x), input().split(' ')))
output_list = list(map(lambda x: int(x), input().split(' ')))
total_queue = [[] for i in range(queue_num)]
index2time = deepcopy(people_waitting)
saver = {}
people_index = 0
for i in range(len(people_waitting)):
    queue_index = i % queue_num
    if len(total_queue[queue_index]) == queue_length  or not people_waitting:
        break
    total_queue[queue_index].append([i,people_waitting.pop(0)])
    people_index = i
# print(total_queue)
while True:
    min_time = sys.maxsize
    pop_queue_index = -1
    for i in range(queue_num):
        if not total_queue[i]: # the queue is empty
            continue
        if total_queue[i][0][1] < min_time:
            min_time = total_queue[i][0][1]
            pop_queue_index = i
    if pop_queue_index == -1:
        break
    reduce_minute = total_queue[pop_queue_index][0][1]
    for i in range(queue_num):
        if not total_queue[i]:
            continue
        total_queue[i][0][1] -= reduce_minute
    now_time += reduce_minute
    success_people = total_queue[pop_queue_index].pop(0)[0]
    saver[success_people] = now_time if now_time - index2time[success_people] < 60 * 9 else 'Sorry'
    # print(now_time - index2time[success_people])
    if people_waitting:
        people_index += 1
        people_used_time = people_waitting.pop(0)
        total_queue[pop_queue_index].append([people_index,people_used_time])
for output in output_list:
    output -= 1
    if saver[output] == 'sorry':
        print(saver[output])
    else:
        sam(saver[output])