#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        flag = 1
        for i in range(n - 1):
            if arr[i] <= arr[i + 1]:
                continue
            else:
                flag = 0
                break
        return flag
            


