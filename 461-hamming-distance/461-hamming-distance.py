class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
       
        temp = bin(x ^ y)[2:]
        counter = Counter(temp)
        return counter["1"]
        