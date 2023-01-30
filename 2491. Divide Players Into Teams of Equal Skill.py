import collections
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
     
        target = sum(skill)//(len(skill)//2)
        cnt = collections.Counter(skill)
        result = 0
        for k, v in cnt.items():
            if target-k not in cnt or cnt[target-k] != cnt[k]:
                return -1
            result += k*(target-k)*v
        return result//2
