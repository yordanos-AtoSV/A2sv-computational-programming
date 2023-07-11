class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        answer = 0
    
        def maxRequest(n, index, count):
            nonlocal answer 
            if index == len(requests):
            
                for i in range(n):
                    if indegree[i] != 0:
                        return

                answer = max(answer, count)
                return

   
            indegree[requests[index][0]] -= 1
            indegree[requests[index][1]] += 1

            maxRequest(n, index + 1, count + 1)

            indegree[requests[index][0]] += 1
            indegree[requests[index][1]] -= 1


            maxRequest(n, index + 1, count)

 
        maxRequest( n, 0, 0)
        
        return answer
 