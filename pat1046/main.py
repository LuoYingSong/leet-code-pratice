dist_list = list(map(lambda x: int(x), input().split(' ')))[1:]
output_pair = []
for _ in range(int(input())):
    i, j = list(map(lambda x: int(x)-1, input().split(' ')))
    if i > j:i,j=j,i
    right = 0
    for k in range(i,j):
        right+=dist_list[k]
    left = 0
    for k in range(0, i):
        left += dist_list[k]
    for k in range(j,len(dist_list)):
        left += dist_list[k]
    print(right if left > right else left)