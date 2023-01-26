n = int(input())

for i in range(n):
    flag = "YES"
    size = int(input())
    array = list(map(int, input().split()))

    array.sort()
    A = set()
    for i in range(size):
        A.add(array[i])
    array = list(A)
    size = len(array)

    for i in range(size-1):
        if array[i+1] - array[i] != 1:
            flag = "NO"
            break
            
    print(flag)
