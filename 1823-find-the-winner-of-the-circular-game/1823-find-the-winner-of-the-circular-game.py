class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [i+1 for i in range(n)]
        i = k - 1
        while len(array) != 1:
            array.pop(i)
            i = (i + k - 1) % len(array) 
        return array[0]

        
