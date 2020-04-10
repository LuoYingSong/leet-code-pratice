inputs = input()
length = len(inputs) + 2
n1 = n2 = length // 3
n3 = length - n1 - n2
n3 -= 2
for i in range(n1-1):
    print(inputs[i]+' '*n3+inputs[-i-1])
print(inputs[i+1:-i-1])