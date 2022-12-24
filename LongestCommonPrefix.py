class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer=min(strs,key=len)

        for i in range(len(answer)):
            for j in strs:
                if i<len(answer) and answer[i]!=j[i]  :
                  answer=answer[:i]
        return answer   
