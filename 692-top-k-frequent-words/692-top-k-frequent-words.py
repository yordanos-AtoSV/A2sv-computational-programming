class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for s in words:
            dic[s]  += 1
            
        heap = []
        
        for word, count in dic.items():
            heappush(heap ,(-count, word))
  
        ans = []
    
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans
