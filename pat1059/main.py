def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True


def find_prime(num):
    ret_list = []
    num2 = num
    while not is_prime(num2) and num2 != 1:
        for i in range(2, num):
            if num2 / i < 1:
                break
            if not num2 % i:
                if is_prime(i) and num2 % i == 0:
                    ret_list.append(i)
                    num2 /= i
                    num2 = int(num2)
                    break
    return ret_list


if __name__ == '__main__':
    num = int(input())
    num2 = num
    outputs = find_prime(num)
    print("{}=".format(num),end='')
    before = -1
    count = 1
    first = 0
    for num in outputs:
        if num == before:
            count += 1
        else:
            if first:
                if count == 1:
                    print("{}*".format(before),end='')
                else:
                    print('{}^{}*'.format(before,count),end='')
            first=1
            before = num
            count = 1
    else:
        for ret in outputs:
            num2 /= ret
        if outputs and num2 != outputs[-1]:
            if count == 1:
                print("{}*{}".format(num,int(num2)))
            else:
                print('{}^{}*{}'.format(num, count,int(num2)))
        else:
            if outputs:
                count += 1
            if count == 1:
                print("{}".format(num))
            else:
                print('{}^{}'.format(num, count))
