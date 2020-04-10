length,index = list(map(lambda x: int(x), input().split(' ')))
total = []
for i in range(length):
    total.append(input())
x_index = {1:[0,6],2:[7,-2],3:[-2,None]}
total = sorted(total,key=lambda x:x[x_index[index][0]:x_index[index][1]]+x[:7])
print('\n'.join(total))