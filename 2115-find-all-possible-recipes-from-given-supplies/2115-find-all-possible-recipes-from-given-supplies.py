class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        q = deque(supplies)
        supplies = set(supplies)
        recipe2 = set(recipes)
        graph = defaultdict(list)
        
        indegree = defaultdict(int)
        
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                
                    
                graph[ing].append(recipes[i])
                if ing not in indegree:
                    indegree[ing] = 0
                indegree[recipes[i]] +=  1
            
            
        # for key in indegree:
        #     if indegree[key] == 0:
        #         q.append(key)
            
            
        while q:
            temp = q.pop()
            if temp not in supplies:
                ans.append(temp)
                
                
            for neigh in graph[temp]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
                    
                    
                    
        return ans