
index2num = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,num):
        if not num % i:
            return False
    return True

def radix_changer(old_num,radix):
    old_num = int(old_num)
    radix = int(radix)
    num_collection = []
    while True:
        num_collection.append(index2num[old_num % radix])
        old_num = old_num // radix
        if not old_num:
            break
    return ''.join(num_collection),''.join(reversed(num_collection))


input_list = []
while True:
    alist = input().split(' ')
    if len(alist) == 1:
        break
    else:
        input_list.append(list(radix_changer(alist[0],alist[1]))+[int(alist[1])])
for num_tuple in input_list:
    if is_prime(int(num_tuple[0],num_tuple[2])) and is_prime(int(num_tuple[1],num_tuple[2])):
        print('Yes')
    else:
        print('No')
