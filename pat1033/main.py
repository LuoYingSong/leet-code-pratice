full, dist2, rate, station = list(map(lambda x:int(x),input().split(' ')))
dist2money = {}
inf = float('inf')
for i in range(station):
    money, dist_ = list(map(lambda x:float(x),input().split(' ')))
    dist2money[dist_] = money
if station == 0:
    exit()
dist2money[dist2] = 0
for key in dist2money.keys():
    if key>dist2:
        del dist2money[key]
moneys = 0
max_dist = rate * full
now_station = 0
remind_oil = 0

while True:
    flag = 0
    able2add = [[key,value] for key,value in dist2money.items() if now_station<key<=now_station+max_dist]
    able2add = sorted(able2add,key=lambda x:x[0])
    for dist_,money in able2add:
        if money < dist2money[now_station]:
            flag = dist_
            break
    if flag:
        moneys += ((flag - now_station) / rate - remind_oil) * dist2money[now_station]
        remind_oil = 0
    else:
        try:
            flag = min(able2add,key=lambda x:x[1])[0]
        except ValueError:
            print('The maximum travel distance = {:.2f}'.format(now_station+max_dist))
            exit()
        moneys += (50-remind_oil) * dist2money[now_station]
        remind_oil = 50 - (flag - now_station) / rate
    now_station = flag
    # print(moneys,now_station)
    if now_station == dist2:
        print("{:.2f}".format(moneys))
        break
        
