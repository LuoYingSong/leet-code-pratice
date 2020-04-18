num_str = input()

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number*factorial(number-1)

def A(n,m):
    return factorial(n)/factorial(n-m)

def find_one(num_str: str) -> int:
    total = 0
    if len(num_str) == 1:
        if int(num_str)>=1:
            return 1
        else:
            return 0
    if int(num_str[0]) == 1:
        return find_one(num_str[1:])
    if int(num_str[0]) > 1:
        '''
        此时就要分析第一位取1和不取1两种情况之和
        '''
        for i in range(0,len(num_str)-1):
            total += 8 ** (len(num_str) - 1 - i) * (int(num_str[0])-1) * i
        for i in range(len(num_str)):
            total += 8 ** (len(num_str)-1-i)*(i+1)
    else:
        total += 1
        for i in range(1,len(num_str)): # i 代表 1出现的次数
            total += i * 8 ** (len(num_str)-1-i) * (len(num_str)-1-i) * A(len(num_str)-1,len(num_str)-1-i)
    return total + find_one(num_str[1:])
