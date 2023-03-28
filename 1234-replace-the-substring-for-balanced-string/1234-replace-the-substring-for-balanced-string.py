class Solution:
    def balancedString(self, s: str) -> int:
            minLength = len(s)


            counter = Counter(s)

            n = int(len(s)/4)

            extra = {}
            for c in counter: 
                if counter[c] > n: 
                    extra[c] = counter[c] - n

            if not extra:
                return 0

            distincts = len(extra)

            l= 0

            for r in range(len(s)):
                if s[r] in extra: 
                    extra[s[r]] -= 1
                    if extra [s[r]] == 0:
                        distincts -= 1

                while distincts == 0:
                    minLength = min(minLength, r - l + 1)
                    if s[l] in extra:
                        extra[s[l]] += 1
                        if extra [s[l]] == 1:
                            distincts += 1 
                    l += 1

                    

            return minLength