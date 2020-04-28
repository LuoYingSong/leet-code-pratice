save_length, a, b = input().split(' ')
save_length = int(save_length)
def translate(str_num):
    num_int = int(float(str_num))
    if num_int != 0:
        pw = len(str(num_int))
    else:
        pw = 0
        flag = 0
        for num in str_num:
            if num == '.':
                pw = 0
            elif flag or (num != '0' and num != '.'):
                break
            else:
                pw -= 1
        if float(str_num) == 0:
            pw = 0
    counter = 0
    index = 0
    ret_string = ''
    flag = 0
    while counter < save_length:
        if index < len(str_num):
            if flag or (str_num[index] != '0' and str_num[index] != '.'):
                flag = 1
                if str_num[index] != '.':
                    counter += 1
                    ret_string += str_num[index]
            index += 1
        else:
            ret_string += '0'
            counter += 1
    return '0.{}*10^{}'.format(ret_string,pw)

if __name__ == '__main__':
    a = translate(a)
    b = translate(b)
    if a == b:
        print('YES',end=' ')
        print(a)
    else:
        print('NO',end=' ')
        print(a,end=' ')
        print(b)
