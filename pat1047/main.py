stu_num, class_num = list(map(lambda x: int(x), input().split(' ')))
if class_num==0 or stu_num==0:
    exit()
saver = dict(zip(range(1,class_num+1),[[]for i in range(class_num)]))
for i in range(stu_num):
    name, *class_list = input().split(' ')
    for the_stu_class in class_list[1:]:
        saver[int(the_stu_class)].append(name)
for i in range(1,class_num+1):
    print(i,len(saver[i]))
    if len(saver[i]):
        print('\n'.join(sorted(saver[i])))