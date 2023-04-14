from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        for num in edges:
            adjlist[num[0]].append(num[1])
            adjlist[num[1]].append(num[0])
      
        for k, v in adjlist.items():
       
            if len(v) == len(adjlist) - 1:
                return k
            