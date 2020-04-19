n, start = list(map(str, input().split(' ')))
n = int(n)
saver = {}
value2addr = {}
for i in range(n):
    addr, value, next = list(map(str, input().split(' ')))
    saver[addr] = [value,next]
    value2addr[value] = addr
data_list = []
next = start
while next != '-1':
    data = saver[next]
    data_list.append(data[0])
    next = data[1]
after_sorted = sorted(data_list,key=lambda x:int(x))
next_data_addr_list = []
for data in after_sorted:
    next_data_addr_list.append(value2addr[data])
next_data_addr_list.append(-1)
print(len(after_sorted),next_data_addr_list[0])
for i in range(len(after_sorted)):
    print('{} {} {}'.format(next_data_addr_list[i],after_sorted[i],next_data_addr_list[i+1]))