# Enter your code here. Read input from STDIN. Print output to STDOUT
def setDifference():
    lenEng=int(input())
    # setA=list(map(int,input().split()))
    setA=set(map(int,input().split()))
    
    lenFren=int(input())
    setB=set(map(int,input().split()))
    
    # setB=list(map(int,input().split()))
    # dict={}
   
    # for i in range(lenFren):
    #     dict[i]=setB[i]

    # for i in range(lenEng):
    #     if setA[i] in dict.values():
    #         del dict[setA[i]]
       
    # print (len(dict))
    
    setC=setA.difference(setB)
 
    print(len(setC))
    
setDifference()
