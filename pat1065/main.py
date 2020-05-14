n = int(input())
for i in range(n):
    a, b, c = list(map(int,input().split(' ')))
    if a+b>c:
        print('Case #{}: true'.format(i+1))
    else:
        print('Case #{}: false'.format(i+1))