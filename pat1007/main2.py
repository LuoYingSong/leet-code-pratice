N = int(input())
nums = [int(i) for i in input().split(" ")]
leftIndex = 0
rightIndex = N - 1
sum = -1  # note this line
tmpSum = 0
tmpIndex = 0
isAllNeg = True
for i in range(N):
    if nums[i] >= 0:
        isAllNeg = False
    tmpSum = tmpSum + nums[i]
    if tmpSum > sum:
        sum = tmpSum
        rightIndex = i
        leftIndex = tmpIndex
    elif tmpSum < 0:
        tmpSum = 0
        tmpIndex = i + 1
if isAllNeg:
    print(0, nums[0], nums[N - 1])
else:
    print(sum, nums[leftIndex], nums[rightIndex])