class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for j in range(len(nums)):
            count = 0
            for i in range(len(nums)):
                if nums[j] > nums[i]:
                    count += 1
            ans.append(count)
        return ans
