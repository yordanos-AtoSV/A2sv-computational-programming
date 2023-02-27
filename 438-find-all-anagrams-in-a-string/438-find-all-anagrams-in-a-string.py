class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_size, p_size = len(s), len(p)
        if s_size < p_size :
            return []
        p_count = Counter(p)
        s_count = Counter()
        result = []
        for i in range(p_size):
            print (p_count.values())
        print(p_count[1])
        for i in range(s_size):
            s_count[s[i]] += 1
            if i >= p_size:
                if s_count[s[i - p_size]] == 1:
                    del s_count[s[i - p_size]] 
                else:
                    s_count[s[i - p_size]] -= 1
            if p_count == s_count:
                result.append (i - p_size + 1)
                
        return result
            
        