n,m = list(map(int, input().split(' ')))
saver = {}
max_num = -1
max_pixel = 0
for i in range(m):
    total_pixel = input().split(' ')
    for pixel in total_pixel:
        try:
            saver[pixel] += 1
        except KeyError:
            saver[pixel] = 1
        if saver[pixel] > max_num:
            max_num = saver[pixel]
            max_pixel = pixel
print(max_pixel)