num2word = dict(zip(list('0123456789')+['10','11','12'],'0123456789ABC'))
num_list = list(map(lambda x: int(x), input().split(' ')))
print("#",end='')
for num in num_list:
    saver = []
    while True:
        if num == 0:
            break
        saver.append(num2word[str(num % 13)])
        num = num // 13
    saver += ['0','0']
    saver = saver[:2]
    print(''.join(reversed(saver)),end='')