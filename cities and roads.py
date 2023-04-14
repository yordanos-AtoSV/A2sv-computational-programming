from collections import defaultdict
n = int(input())
matrix = []
for _ in range(n):
    arr = list(map(int, input().split()))
    matrix.append(arr)

adjlist= defaultdict(set)
count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            count += 1

print(count // 2)
