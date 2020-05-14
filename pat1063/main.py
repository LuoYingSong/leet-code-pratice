n = int(input())
datas = []
for i in range(n):
    datas.append(set(list(map(int, input().split()))[1:]))
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    s1 = datas[a-1]
    s2 = datas[b-1]
    rate = len(s1&s2)/(len(s1)+len(s2)-len(s1&s2))
    print("{:.1f}%".format(round(rate,3)*100))