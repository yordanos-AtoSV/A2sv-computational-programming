class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = ["a","e","i","o","u"]
        allPath = []
        
        def back(k,i, path):
            if k == n:
                allPath.append(''.join(path))
                return
            
            for j in range(i,len(a)):
                # path.append(a[j])
                back(k+1, j,path+[a[j]])
                # path.pop()
        
        for i in range(len(a)):
            back(1,i,[a[i]])
        
        return len(allPath)