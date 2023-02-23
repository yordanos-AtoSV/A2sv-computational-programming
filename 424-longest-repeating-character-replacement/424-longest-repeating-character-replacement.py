class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        maxcount = 0
        left = 0
        window = defaultdict(int)
        
        for i in range(length):
            window[s[i]] += 1
            maxFreq = max(window.values())
            while (i - left + 1) - maxFreq> k:
                window[s[left]] -= 1
                left += 1
            maxcount = max(maxcount, i - left+ 1)

        return maxcount