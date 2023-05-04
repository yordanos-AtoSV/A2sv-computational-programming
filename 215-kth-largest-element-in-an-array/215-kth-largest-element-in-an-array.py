import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        n = len(nums) - (k)
        for i in range(n):
            heappop(nums)
        
        return nums[0]
            
        
        
        
        
        
        
#         def heapify(nums):
#             n = len(nums)
#             for i in range(n // 2 - 1, -1, -1):
#                 heapify_down(nums, n, i)
#             print(nums)
#             return heap_sort(nums, n)

            
#         def heapify_down(nums, n, i):
#             left = (2 * i) + 1
#             right = (2 * i) + 2 

#             while (n > left and nums[i] < nums[left]) or (n > right and nums[i] < nums[right]):
#                 if n > left and n > right:
#                     if nums[left] > nums[right]:
#                         max_child = left
#                     else:
#                         max_child = right

#                 elif n > left:
#                     max_child = left
#                 else:
#                     max_child = right

#                 nums[i], nums[max_child] = nums[max_child], nums[i]
#                 i = max_child
#                 left = (2 * i) + 1
#                 right = (2 * i) + 2
                
                
#         def heap_sort(nums, n):
#             for i in range(k):
#                 ptr = n - 1
#                 nums[ptr], nums[0] = nums[0], nums[ptr]
#                 ptr -= 1
#                 heapify_down(nums, ptr, 0)
#                 print(nums)
                
                
#             return nums[k - 1]

 
#         return heapify(nums)
        
        
