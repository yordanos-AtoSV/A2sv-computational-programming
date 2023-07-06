# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr)   
        p1, p2 = 0, n - 1
        
        maxim = 0
        for i in range(n//2):
            maxim = max(maxim, arr[p1] + arr[p2])
            p1 += 1
            p2 -= 1
            
        return maxim
            