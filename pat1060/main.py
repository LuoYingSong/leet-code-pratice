save_length, a, b = input().split(' ')
save_length = int(save_length)
# f_a, f_b = float(a), float(b)
# a,b = str(f_a),str(f_b)

try:
    ptr_index_a = a.index('.')
except ValueError:
    ptr_index_a = len(a)
try:
    ptr_index_b = b.index('.')
except ValueError:
    ptr_index_b = len(b)
a = a.replace('.','')
b = b.replace('.','')
a += "".join(['0' for i in range(1000)])
b += ''.join(['0' for i in range(1000)])
offset = 0
for num in a:
    if num == '0':
        offset += 1
    else:
        break
if offset == len(a):
    offset = 1
if a[offset:save_length+offset] == b[offset:save_length+offset] and ptr_index_a == ptr_index_b:
    # if a[0] == '0':
    #     ptr_index_a -= 1
    # if b[0] == '0':
    #     ptr_index_b -= 1
    print('YES',end=' ')
    print('0.{}*10^{}'.format(a[offset:save_length+offset],ptr_index_a-offset))
else:
    # if a[0] == '0':
    #     ptr_index_a -= 1
    # if b[0] == '0':
    #     ptr_index_b -= 1
    print('NO', end=' ')
    print('0.{}*10^{}'.format(a[offset:save_length+offset], ptr_index_a-offset),end=' ')
    print('0.{}*10^{}'.format(b[offset:save_length+offset], ptr_index_b-offset))