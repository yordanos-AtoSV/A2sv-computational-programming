class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = None 
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        if index == None:
            return r + 1
        else:
            return index
                
        