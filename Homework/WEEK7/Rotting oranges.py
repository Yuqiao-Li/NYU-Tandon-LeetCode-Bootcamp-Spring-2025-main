class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        
        while rotten and fresh_count > 0:
            minutes += 1
            new_rotten = []
            
            for r, c in rotten:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == 1):
                        grid[nr][nc] = 2  
                        fresh_count -= 1
                        new_rotten.append((nr, nc))
            
            rotten = new_rotten
        
        return minutes if fresh_count == 0 else -1