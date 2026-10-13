from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #get dimensions
        rows = len(grid)
        cols = len(grid[0])

        #time in minutes
        time = 0

        fresh = 0

        queue = deque()
        #loop through the whole thing to get the number of rotten and fresh fruit
        for r in range(rows) :
            for c in range(cols) :
                #rotten
                if grid[r][c] == 2 :
                    #add these to the queue
                    queue.append((r, c))
                elif grid[r][c] == 1 :
                    fresh += 1

        #the only ways the loop ends is if the queue is empty or the fresh fruits becomes 0   
        while queue and fresh > 0 :
            #remove all the rotten fruit in the queue rn
            for i in range(len(queue)) :
                r, c = queue.popleft()
                #check adjacent fruits
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions :
                    #check if in bounds and if fruits are fresh
                    if dr + r in range(rows) and dc + c in range(cols) and grid[dr + r][dc + c] == 1 :
                        #mark it as rotten/visisted
                        grid[dr + r][dc + c] = 2
                        queue.append((dr + r,dc + c))
                        fresh -= 1
            time += 1
        
        #either all fruits are rotten or there are still some fresh ones
        if fresh == 0 :
            return time
        else :
            return -1



