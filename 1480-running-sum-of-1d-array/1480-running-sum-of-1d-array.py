class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        prefsum = []
        for i in range(len(nums)):
                prev += nums[i]
                prefsum.append(prev)
        return prefsum