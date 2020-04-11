num_list = sorted(list(map(str, input().split(' ')))[1:])
string = ''
while num_list:
    first_num = num_list[0]
    if len(num_list)>1:
        if first_num + num_list[1] > num_list[1] + first_num:
            string += num_list.pop(1)
        else:
            string += num_list.pop(0)
    else:
        string += num_list.pop(0)
print(int(string))
