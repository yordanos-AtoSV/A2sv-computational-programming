# Enter your code here. Read input from STDIN. Print output to STDOUT
def setUnion():
    lenEng=int(input())
   
    setA=set(map(int,input().split()))
    
    lenFren=int(input())
    setB=set(map(int,input().split()))
    setC=setA.union(setB)
 
    print(len(setC))
    
setUnion()
