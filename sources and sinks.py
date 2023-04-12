n = int(input())
arr = []

for i in range(n):
    temp = list(map(int, input().split())) 
    arr.append(temp)
notsource = set()
notsink = set()   
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
             notsink.add(i + 1)


for i in range(len(arr)):
    for j in range(len(arr[0])):
         if arr[j][i] == 1:
            notsource.add(i + 1)
source = []
sink = []
for i in range(1, n + 1):
    if i not in notsource:
        source.append(i)
    if i not in notsink:
        sink.append(i)     


source.sort()
sink.sort()

print(len(source), " ".join(map(str,source)))
print(len(sink), " ".join(map(str, sink)))
