import math

def countMAxSubsequence(arr, length):
    positive = False
    if arr[0] > 0:
        positive = True

    if arr[-1] > 0:
        arr.append(-1)
    else:
        arr.append(1)

    maxVal = 0
    minVal = -math.inf
    res = 0
    for i in range(length):
        if arr[i] > 0:
            maxVal = max(maxVal, arr[i])
        elif positive and arr[i] < 0:
            res += maxVal
            positive = False
            maxVal = 0

        if arr[i] < 0:
            minVal = max(minVal, arr[i])
        elif not positive and arr[i] > 0:
            res += minVal
            minVal = -math.inf
            positive = True
    if positive:
        res += maxVal
    else:
        res += minVal
    return res


size = int(input())
for i in range(size):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    print(countMAxSubsequence(arr, length))
