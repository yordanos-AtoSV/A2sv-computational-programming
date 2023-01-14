class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        common = Counter(words[0])
        for word in words:
            temp = {}
            word = Counter(word)
            for key in word:
                if key in common:
                    temp[key] = min(word[key], common[key])
            common = temp
        for key in common:
            for i in range(common[key]):
                ans.append(key)
        return ans
              
        
       
