from collections import defaultdict
n = int(input())
adjlist = defaultdict(list)
matrix = []
for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            adjlist[i + 1].append(j + 1)

for num in adjlist.values():
    print(len(num), " ".join(map(str, num)))             
