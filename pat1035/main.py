n = int(input())
id_pwd_list = []
for i in range(n):
    id_, pwd = input().split(' ')
    new_pwd = pwd.replace('1','@').replace('0','%').replace('l','L').replace('O','o')
    if new_pwd != pwd:
        id_pwd_list.append([id_,new_pwd])
if not id_pwd_list:
    if n > 1 :
        print('There is {} accounts and no account is modified'.format(n))
    else:
        print('There are {} account and no account is modified'.format(n))
else:
    print(len(id_pwd_list))
    for item in id_pwd_list:
        print(' '.join(item))