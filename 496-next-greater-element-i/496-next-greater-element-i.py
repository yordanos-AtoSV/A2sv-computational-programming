class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []
        
        dic = defaultdict(int)
        for i in range(len(nums1)):
            dic[nums1[i]] = i

        for c in nums2:
            if len(stack) != 0:
                if stack[-1] > c:
                    stack.append(c)
                else:
                    while len(stack) != 0 and stack[-1] < c:
                        if stack[-1] in nums1:
                                ans[dic[stack[-1]]] = c
                          
                        stack.pop()
                
            stack.append(c)
            
        return ans
        
                        
                    