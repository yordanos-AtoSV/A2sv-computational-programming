n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
p1, p2 = 0, 0
res = [0] * m

while p2 < m:

    if p1 < n:
        
        while p1 < n and arr2[p2] > arr1[p1]:
            p1 += 1
            
        res[p2] = p1 
        p2 += 1
        
        
    else:
        res[p2] = p1
        p2 += 1
        
        
    
    
print(" ".join(map(str, res)))
        
