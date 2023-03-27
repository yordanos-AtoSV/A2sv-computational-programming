class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        maps = {'2':"abc", '3': "def",'4': "ghi", '5': "jkl", '6': "mno",  '7': "pqrs" ,
               '8': "tuv" , '9': "wxyz"}
        
        if len(digits) == 0:
            return []
        
        def back(index, path):
            if index == len(digits):
                ans.append("".join(path))
                return 
            for c in maps[digits[index]]:
                path.append(c)
                back(index + 1, path)
                path.pop()
                
        back(0,[])
                
        return ans