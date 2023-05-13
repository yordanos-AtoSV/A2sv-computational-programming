#User function Template for python3
from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for i in range(n - 1):
            size = min(len(alien_dict[i]), len(alien_dict[i + 1]))
            for s in range(size):
                if alien_dict[i][s] != alien_dict[i + 1][s]:
                    graph[alien_dict[i][s]].append(alien_dict[i + 1][s])
                    incoming[alien_dict[i + 1][s]] += 1
                    break

        visited = set()
        q = []
        ans = []
        
        def dfs(node, ans):
            if node in visited:
                return
            
            for neigh in graph[node]:
                dfs(neigh, ans)
                
            visited.add(node)
            ans.append(node)
            return 

       
        for i in range(ord("a") , ord("a")  + k):
            letter = chr(i)
            if incoming[letter] == 0:
                q.append(letter)
                
                
        for let in q:
            dfs(let, ans)
            
        ans.reverse()
        return ans
                
            
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
