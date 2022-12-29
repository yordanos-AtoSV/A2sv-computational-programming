class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer=[]
        j=""
        longer=max(word1,word2,key=len)
        
        for i in range(len(longer)):
            if i<len(word1):
               answer.append(word1[i])
            if i<len(word2):
               answer.append(word2[i])
        for i in answer:
            j+=i
        return j
    
