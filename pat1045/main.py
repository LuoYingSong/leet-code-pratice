input()
order_list = list(map(lambda x: int(x), input().split(' ')))[1:]
stripe_colors = list(map(lambda x: int(x), input().split(' ')))[1:]
saver = [0 for i in range(len(order_list))]
for color in stripe_colors:
    if color in order_list:
        index = order_list.index(color)
        saver[index] = max(saver[:index+1]) + 1
print(max(saver))
