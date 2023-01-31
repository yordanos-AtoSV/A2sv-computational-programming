from collections import defaultdict
n, m= map(int,input().split())

grid = []
for i in range(n):
    inputStr, outputStr = input(), ''
    for i in range(len(inputStr)): 
        
        if i == len(inputStr) - 1:
            outputStr += inputStr[i] 
        else:
            outputStr += inputStr[i] + ','
   
    array = list(map(str,outputStr.split(',')))
    grid.append(array)
row = defaultdict(list)
col = defaultdict(list)

for i in range(n):
    for j in range(m):
        row[i].append(grid[i][j])
        col[j].append(grid[i][j])

ans = []

for i in range(n):
    
    for j in range(m):
        countr = 0
        countc = 0
    
        for x in row[i]:
          

            if grid[i][j] == x:
                

                countr += 1
     
        for x in col[j]:
            

            if grid[i][j] == x:
                
                countc += 1

        if countr == 1 and countc == 1:
            
            
            ans.append(grid[i][j])
        else:
            continue
print("".join(ans))
