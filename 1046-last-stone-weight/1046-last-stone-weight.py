class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heappush(heap, -num)
            
            
        while len(heap) >= 2:
            num1 = heappop(heap)
            num2 = heappop(heap)
            
            if num1 == num2:
                continue
            else:
                heappush(heap, (-num2) - (-num1))
                
        return 0 if not heap else -heap[0]