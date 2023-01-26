class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)

        size = len(piles)
        x= size//3
        y = size  - x
        sum = 0
        for i in range(1, y, 2):
            
            sum += piles[i]
        return sum
