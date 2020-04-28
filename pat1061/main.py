from string import ascii_lowercase, ascii_uppercase

str1 = input()
str2 = input()
length = min(len(str1), len(str2))
flag = 0
index2day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
hour = '0123456789' + ascii_uppercase[:14]
for char1, char2 in zip(str1[:length], str2[:length]):
    if char1 == char2:
        if char1 in ascii_uppercase[:7] and not flag:
            flag = 1
            print(index2day[ascii_uppercase.index(char1)], end=' ')
        elif flag and char1 in hour:
            print('{:0>2d}:'.format(hour.index(char1)), end='')
            break
str1 = input()
str2 = input()
length = min(len(str1), len(str2))
for char1, char2, i in zip(str1[:length], str2[:length], range(length)):
    if char1 == char2 and ( char1 in ascii_uppercase or char1 in ascii_lowercase):
        print('{:0>2d}'.format(i))
        break