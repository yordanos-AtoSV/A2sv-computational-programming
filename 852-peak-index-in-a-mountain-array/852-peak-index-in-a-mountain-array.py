class Solution:
      def peakIndexInMountainArray(self, arr: List[int]) -> int:
            stack = []
            for i in range(len(arr)):
                if stack and arr[stack[-1]] > arr[i]:
                    return stack[-1]
                
                stack.append(i)
                    

