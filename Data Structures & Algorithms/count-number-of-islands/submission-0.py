from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        #need to mark positions as visisted
        visited = set()
        islands = 0

        def bfs(r, c) :
            queue = deque()
            #mark as visited
            visited.add((r, c))
            queue.append((r, c))

            while(queue) :
                node = queue.popleft()
                r = node[0]
                c = node[1]
                #check adjacent nodes
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr, dc in directions :
                    #check if in grid
                    if r + dr in range(rows) and c + dc in range(cols) and grid[dr+r][dc+c] == "1" and (dr + r, c + dc) not in visited:
                        #add to the queue
                        queue.append((r + dr, c + dc))
                        #mark it visited
                        visited.add((r + dr, c + dc))


        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == "1" and (r, c) not in visited:
                    #run BFS
                    bfs(r, c)
                    islands += 1
        return islands