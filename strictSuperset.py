# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def sets():
   
    A=set(map(int, input().split()))
    
    n=int(input())
    flag=[]
    count=0

    
    for i in range(n):
        
        B=set(map(int, input().split()))
       
        if A.issuperset(B):
            flag.append(True)
        
        else:
            flag.append(False)
            
    for i in flag:
        if i==False:
            count+=1
    if count==0:
        print(True)
    else:
        print(False)
        


       
sets()
