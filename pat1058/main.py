a, b = input().split(' ')
is_plus_one = 0
rate_list = [float('inf'),17,29]
outputs = []
for i,j,rate in reversed(list(zip(a.split('.'),b.split('.'),rate_list))):
    total = int(i) + int(j) + is_plus_one
    if total >= rate:
        total -= rate
        is_plus_one = 1
    else:
        is_plus_one = 0
    outputs.append(str(total))
print('.'.join(reversed(outputs)))