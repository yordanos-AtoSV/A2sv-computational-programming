class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts=collections.Counter()
        MOD=10**9+7

        total=0
        for x in deliciousness:
            for y in range(22):
                target=(1<<y)-x

                if target in counts:
                    total+=counts[target]
            counts[x]+=1
        return total%MOD
