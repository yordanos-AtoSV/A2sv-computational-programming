class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2:
            return []
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        visited = set()
        while heap and len(res) < k:
            
            _, i, j = heapq.heappop(heap)
            res.append((nums1[i], nums2[j]))
            
            if i < len(nums1)-1 and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
                
            if j < len(nums2)-1 and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
                
        return res