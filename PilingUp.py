# Enter your code here. Read input from STDIN. Print output to STDOUT
def PilingUp():
    testcase=int(input())
    for i in range(testcase):
        size=int(input())
        block=list(map(int,input().split()))
        
        
        leftptr=0
        rightptr=size-1
        previous=float("inf")
        
        flag="Yes"
        
        while(leftptr<=rightptr):
            if block[leftptr]>=block[rightptr]:
                if previous<block[leftptr]:
                    flag="No"
                    break
                previos=block[leftptr]    
                leftptr+=1
            else:
                if previous<block[rightptr]:
                    flag="No"
                    break
                previous=block[rightptr]
                rightptr-=1
        print(flag)
PilingUp()
            
            
            
            
        
