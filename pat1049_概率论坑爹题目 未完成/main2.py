# n = int(input())
#34567 -> 30000
#20
def func(n):
    str_num = str(n)
    count = 0
    for i in range(len(str_num)):
        num = int(str_num[:i]+str_num[i+1:])
        count += num
    return count


if __name__ == '__main__':
    print(func(19))