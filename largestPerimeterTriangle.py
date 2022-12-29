class Solution:
    def checkArea(self, a:int, b:int, c:int):
        s=(a+b+c)/2
        area=-1
        if s>=a and s>=b and s>=c:
          area=sqrt(s*(s-a)*(s-b)*(s-c))

        print(area)
        return area>0


    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n-2):
            a=nums[i]
            b=nums[i+1]
            c=nums[i+2]
            if self.checkArea(a,b,c):
                return a+b+c

        return 0
