num,step = list(map(lambda x: int(x), input().split(' ')))

num = str(num)
flag = 1
if num == ''.join(reversed(num)):
    print(num)
    print(0)
else:
    for i in range(step):
        resered = ''.join(reversed(num))
        num = str(int(num) + int(resered))
        if num == ''.join(reversed(num)):
            print(num)
            print(i+1)
            flag = 0
            break
    if flag:
        print(num)
        print(step)
