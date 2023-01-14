from collections import defaultdict
n = int(input())
for i in range(n):
    n,m = map(int,input().split())
    matrix = []
    maximum=0
    forward = defaultdict(int)
    reverse = defaultdict(int)
    for i in range(n):
        temp=list(map(int,input().split()))
        matrix.append(temp)
    
    for i in range(n):
        for j in range(m):
            
            ward = i-j
            re = i+j
            
            forward[ward] += matrix[i][j]   
            reverse[re] += matrix[i][j]  
    for i in range(n):
        for j in range(m):
            
            ward = i-j
            re = i+j     
            temp = forward[ward] + reverse[re] - matrix[i][j]
            maximum = max(maximum, temp)
    print(maximum)
