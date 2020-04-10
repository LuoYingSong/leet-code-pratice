data_num, queue_length = list(map(lambda x:int(x),input().split(' ')))
time2wait_time = {}
for i in range(data_num):
    time, wait_time = input().split(' ')
    time2wait_time[time] = float(wait_time)
for time in sorted(time2wait_time.keys()):
    print(time,time2wait_time[time])