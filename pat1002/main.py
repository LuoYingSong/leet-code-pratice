if __name__ == "__main__":
    a = [0 for i in range(1001)]
    s1 = [2, 1, 2.4, 0, 3.2]
    s2 = [2, 2, 1.5, 1, 0.5]
    for i in range(int(s1[0])):
        a[int(s1[i * 2 + 1])] += float(s1[i * 2 + 2])
    for i in range(int(s2[0])):
        a[int(s2[i * 2 + 1])] += float(s2[i * 2 + 2])
    countNo = 0
    for i in range(1001):
        if a[i]:
            countNo += 1
    if countNo:
        print(countNo, end=" ")
    else:
        print(countNo)
    for i in range(1000, -1, -1):
        if a[i]:
            countNo -= 1
            if countNo > 0:
                print(i, round(a[i], 1), end=" ")
            else:
                print(i, round(a[i], 1))