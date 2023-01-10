class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in range(len(paths)):
            li=paths[i].split()
            for i in range(1, len(li)):
                content=li[i].split("(")
                
                key = content[1][:len(content[1])-1]
                value=li[0]+"/"+content[0]
                dic[key].append(value)
        ans=[]
        for key in dic:
            if len(dic[key])>1:
                ans.append(dic[key])
        return ans
