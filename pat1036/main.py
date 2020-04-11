n = int(input())
lowerest_male = [float('inf')]
highest_female = [-1]
for i in range(n):
    name, sex, iD, rank = input().split(' ')
    rank = int(rank)
    if sex == 'M':
        if rank < lowerest_male[-1]:
            lowerest_male = [name, iD, rank]
    if sex == 'F':
        if rank > highest_female[-1]:
            highest_female = [name, iD, rank]
f1, f2 = 0, 0
if len(highest_female) > 1:
    print(' '.join(highest_female[:-1]))
    f1 = 1
else:
    print('Absent')
if len(lowerest_male) > 1:
    print(" ".join(lowerest_male[:-1]))
    f2 = 1
else:
    print('Absent')
if f1 and f2:
    print(highest_female[-1]-lowerest_male[-1])
else:
    print('NA')