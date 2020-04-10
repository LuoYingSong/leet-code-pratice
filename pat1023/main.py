def f(num):
    saver = {}
    for i in str(num):
        if i not in saver:
            saver[i] = 1
        else:
            saver[i] += 1
    return saver

num = input()
dict1 = f(num)
double_num = int(num)*2
dict2 = f(double_num)
print("Yes" if dict1 == dict2 else "No")
print(double_num)