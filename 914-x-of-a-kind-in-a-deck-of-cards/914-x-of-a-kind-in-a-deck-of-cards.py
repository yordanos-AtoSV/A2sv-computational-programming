from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        arr = list(count.values())
        Gcd = 0
        if len(arr) == 1:
            hcf = arr[0]
        else:    
            Gcd = gcd(arr[0], arr[1])
            if len(arr) == 2:
                hcf = Gcd
            else:
                for i in range(2, len(arr)):
                    Gcd = math.gcd(Gcd, arr[i])
                    if Gcd == 1:
                        hcf = 1
                hcf = Gcd 
        if hcf > 1:
            return True
        return False
        