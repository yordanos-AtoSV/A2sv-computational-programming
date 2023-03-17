class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #empty list for answer
        ans_arr=[]
        #loop through nums1
        for i in nums1:
            #default value for answer (if no greater val found)
            ans = -1
            #find the index of that number within nums2
            index_two = nums2.index(i)
            #temp array: slice off the rest of the array after the index
            temp = nums2[index_two+1:]
            #loop through temp array
            for j in temp:
                #if item in temp is greater than i
                if j > i:
                    #make that the answer
                    ans = j
                    #break the loop (we only need to find the first greater value)
                    break
            #add ans to the answer array - if we havent found a greater val it'll still be -1
            ans_arr.append(ans)
        #bring it home
        return ans_arr