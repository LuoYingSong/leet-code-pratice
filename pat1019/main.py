# num_abc = dict(zip(range(16),list('0123456789abcdef')))
def trans(num,dec):
    if num == 0:
        return 'Yes','0'
    saver = []
    while True:
        saver.append(str(num % dec))
        num = num // dec
        if num == 0:
            break
    for i in range(0,len(saver)//2):
        if saver[0] != saver[len(saver)-1-i]:
            return 'No', ' '.join(reversed(saver))
    return 'Yes', ' '.join(reversed(saver))
num, dec = list(map(lambda x:int(x),input().split(' ')))
result = trans(num, dec)
print(result[0])
print(result[1],end='')