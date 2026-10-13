from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we will run a bfs starting at the rotten fruit

        #so lets first loop through the entire grid 
        #to find all the rotten fruits

        rows = len(grid)
        cols = len(grid[0])

        #keep track of the number of fresh fruits as well
        fresh = 0

        #queue for bfs
        queue = deque()
        for r in range(rows) :
            for c in range(cols) :
                #check if curren cell is rotten
                if grid[r][c] == 2 :
                    #rotten
                    queue.append((r, c))
                elif grid[r][c] == 1 :
                    fresh += 1
        #track minutes
        time = 0
        while queue and fresh > 0:
            #remove all rotten from the queue
            for i in range(len(queue)) :
                r, c = queue.popleft()
                #get adjacent fresh
                directions = [[0,-1], [0,1], [-1,0], [1,0]]
                for dr, dc in directions :
                    if dr + r in range(rows) and dc + c in range(cols) and grid[dr + r][dc + c] == 1 :
                        #mark as rotten
                        grid[dr + r][dc + c] = 2
                        #add to the queue
                        queue.append((dr + r, dc + c))
                        fresh -= 1
            time += 1

        #check if all fruits are rotten
        if fresh == 0 :
            return time
        else :
            return -1


        