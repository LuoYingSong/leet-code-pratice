data_list = []
index2game_result = {0:'W',1:'T',2:'L'}
while True:
    try:
        data = input().split(' ')
        if len(data) != 3:
            break
        data_list.append(list(map(lambda x:float(x),data)))
    except:
        break
goal_list = []
hist_result = []
for data in data_list:
    goal_list.append(max(data))
    hist_result.append(index2game_result[data.index(max(data))])
print(' '.join(hist_result),end=' ')
from functools import reduce
num = (reduce(lambda x,y:x*y,goal_list)*0.65 - 1)*2
print(round(num,2))
