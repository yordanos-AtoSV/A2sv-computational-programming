class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        visited = set() 
        N = len(image) - 1
        n = len(image[0]) - 1

        def dfs(visited, x, y):  #function for dfs 
            if (x,y) not in visited:
                visited.add((x,y))
                g, h, d, b = max(0, x - 1), max(0, y - 1), min(N, x + 1), min(n, y + 1)
                if image[g][y] == init_color:
                     dfs(visited, g, y)
                if image[x][h] == init_color:
                     dfs(visited, x, h)
                if image[d][y] == init_color:
                     dfs(visited, d, y)
                if image[x][b] == init_color:
                     dfs(visited, x, b)
                if image[x][y] == init_color:
                    image[x][y] = color

        dfs(visited, sr, sc)
        return image