_, course_num = list(map(int, input().split(' ')))
stu_info = {}
for i in range(course_num):
    class_num,  _ = list(map(int, input().split(' ')))
    if not _:
        continue
    stu_list = input().split(' ')
    for stu in stu_list:
        try:
            stu_info[stu].append(class_num)
        except KeyError:
            stu_info[stu] = [class_num]
output_list = input().split(' ')
for stu in output_list:
    print(stu,end=' ')
    if stu in stu_info:
        print(len(stu_info[stu]),end=' ')
        print(' '.join(map(str,sorted(stu_info[stu]))))
    else:
        print(0)