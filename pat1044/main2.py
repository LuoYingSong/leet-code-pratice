n, m = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

s = [0]
total = 0
for dia in d:
    total += dia
    s.append(total)

mini = 10 ** 8
pairs = []

j = 0
for i in range(1, n + 1):

    # 注意下面的循环会使j沿一个方向一直移动到n，所有i遍历完成后总的时间复杂度为O(n)
    while j <= n and s[j] - s[i - 1] < m:
        j += 1

    if j > n:
        break
    if s[j] - s[i - 1] < mini:
        pairs.clear()
        pairs.append((i, j))
        mini = s[j] - s[i - 1]
    elif s[j] - s[i - 1] == mini:
        pairs.append((i, j))

for i, j in pairs:
    print("%d-%d" % (i, j))