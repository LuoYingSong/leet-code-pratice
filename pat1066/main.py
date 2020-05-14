n = input()
data_list = list(map(int,input().split(' ')))
length = len(data_list)
n2 = len(bin(length).split('b')[-1]) - 2
n2 = 0 if n2 <= 0 else n2
if length - 2 ** n2 >= 2 ** (n2+1):
    rage = length - 2 ** n2 - (2 ** (n2+1)-1)
    mid = length - 2 ** n2 - (rage)
else:
    mid = length - 2 ** n2
print(data_list[mid])