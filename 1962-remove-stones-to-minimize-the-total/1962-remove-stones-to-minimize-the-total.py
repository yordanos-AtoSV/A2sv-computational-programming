class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
            
        heapify(piles)
        for i in range(k):
            temp = heappop(piles)
            new = floor(temp / 2)
            heappush(piles, new)
            

            
        return -sum(piles)
            
            
        