case = int(input())
for i in range(case):

    a, b = map(int, input().split())    
    
    min1 = min(a, b)
    team = (a + b) // 4
    
    print(min(min1, team))
    
     
