data = input().split(' ')
index = int(data[2])-1
data2 = dict(zip([str(i) for i in range(0,10)]+list('abcdefghijklmnopqrstuvwxyz'),list(range(0,36))))
if data[0] == data[1]:
    print(data[-1],end='')
def int2(num_str,n):
    sum_ = 0
    num_list = list(num_str)
    num_list.reverse()
    for i,num in enumerate(num_list):
            sum_ += n**i * data2[num]
    return sum_
if index == 0:
    num0 = int2(data[0],int(data[-1]))
    num1 = data[1]
else:
    num0 = int2(data[1], int(data[-1]))
    num1 = data[0]
if data2[max(list(num1))]+1 > num0:
    print('Impossible', end='')
    exit()
start = data2[max(list(num1))]
end = num0 + 1
while True:
    mid = start + (end-start) // 2
    num_10 = int2(num1,mid)
    if num_10 > num0:
        end = mid
    elif num_10 < num0:
        start = mid
    else:
        print(mid,end='')
        break
    if end == start + 1:
        # num_10 = int2(num1,start)
        # if num_10 == num0:
        #     print(start,end='')
        # else:
        #     num_10 = int2(num1, end)
        #     if num_10 == num0:
        #         print(end, end='')
        #     else:
        print('Impossible', end='')
        break
