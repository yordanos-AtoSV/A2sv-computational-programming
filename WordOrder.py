# Enter your code here. Read input from STDIN. Print output to STDOUT
def wordOrder():
    n=int(input())
    arry=[]
    for i in range(n):
        arry.append(input())
    hash={}  
    for i in range(len(arry)):
        if arry[i] in hash:
            hash[arry[i]]+=1
        else:
            hash[arry[i]]=1
    print(len(hash))
    print(*hash.values())
    
        
wordOrder()
