class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        a,b,space,count=0,0,[],0
        while b<len(chars):
            if chars[a]==chars[b]:
                b+=1
                count+=1
            elif chars[a]!=chars[b]:
                if count==1:
                    space.append(chars[a])
                else:
                    space.extend([chars[a]]+list(str(count)))
                a=b
                count=0
            
        if count==1:
            space.append(chars[a])
        else:
            space.extend([chars[a]]+list(str(count)))
       
            
        chars[:]=space           
        return len(chars)

