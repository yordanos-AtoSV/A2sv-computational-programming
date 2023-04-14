from collections import defaultdict
vertices = int(input())
operation = int(input())
adjlist = defaultdict(list)
for i in range(operation):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        adjlist[temp[1]].append(temp[2])
        adjlist[temp[2]].append(temp[1])


    else:
        if adjlist[temp[1]]:
            print(" ".join(map(str,adjlist[temp[1]])))
