class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        k=0
        j=size-1
        if size%2==0:
            n=int(size/2)
        else:
            n=int(math.floor(size/2))

        for i in range(n):
            s[k],s[j]=s[j],s[k]
           
            k+=1
            j-=1


        return s
