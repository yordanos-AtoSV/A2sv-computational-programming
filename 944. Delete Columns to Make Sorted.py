class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
         
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i])

            tempsorted = sorted(temp)
     
            if temp != tempsorted:
                count += 1
        return count
