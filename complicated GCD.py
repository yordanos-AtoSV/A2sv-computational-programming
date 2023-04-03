
a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
        
    return gcd(b, a % b)
    
gcd = gcd(a, b)    


for i in range(a, b + 1):
    def calcugcd(a, b):                          
        if b == 0:
            return a
            
        return calcugcd(b, a % b)
        
    gcd = calcugcd(gcd, i)
    if gcd == 1:
        break
    
print(gcd)
    
