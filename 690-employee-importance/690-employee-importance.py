"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id:e for e in employees }
        def dfs(e):
            count = emap[e].importance
            for subs in emap[e].subordinates:
                count += dfs(subs)
                
            return count
            
        return dfs(id)    