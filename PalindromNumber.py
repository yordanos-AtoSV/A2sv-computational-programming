class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1=str(x)
    
        list2=list1[::-1]
        

        if list1!=list2:
            return False
        else:
           return True
