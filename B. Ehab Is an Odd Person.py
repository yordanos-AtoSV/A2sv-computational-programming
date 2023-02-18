

n = int(input())
array = list(map(int, input().split()))
oddeven = [False, False]

for i, c in enumerate(array):
    if c % 2 != 0:
        oddeven[0] = True
    else:
        oddeven[1] = True
if oddeven[0] and oddeven[1]:
    array.sort()
print(" ".join(map(str, array)))
        
    
    

    


        
        
        
    
    



