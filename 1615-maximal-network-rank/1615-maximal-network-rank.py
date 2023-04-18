class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjmatrix = [[ 0 for i in range(n)] for i in  range(n)]

        for num in roads:
            adjmatrix[num[0]][num[1]] = 1
            adjmatrix[num[1]][num[0]] = 1 
            
        nwrank = 0    
        for i in range(n):
            count = Counter(adjmatrix[i])
            count1 = count[1]
            for j in range(i + 1, n):
                count2 = Counter(adjmatrix[j])
                count12 = count2[1]
                if adjmatrix[i][j] == 1 or adjmatrix[j][i] == 1:
                    nwrank = max(nwrank, (count1 + count12) - 1 )
    
                else:
                    nwrank = max(nwrank, count1 + count12)
    
                    
                    
        return nwrank
                
                
            
        