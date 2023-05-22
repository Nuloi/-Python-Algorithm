def count_grass_clumps(grid, R, C):
    visited = [[False] * C for _ in range(R)]  
    count = 0  

    def is_valid_cell(row, col):
        return 0 <= row < R and 0 <= col < C and grid[row][col] == '#' and not visited[row][col]

    def explore_grass_clump(row, col):
        visited[row][col] = True


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_cell(new_row, new_col):
                explore_grass_clump(new_row, new_col)

    for row in range(R):
        for col in range(C):
            if is_valid_cell(row, col):
                count += 1
                explore_grass_clump(row, col)

    return count

R, C = map(int, input().split())

grid = []
for _ in range(R):
    row = input().strip()
    grid.append(row)

clump_count = count_grass_clumps(grid, R, C)

print(clump_count)
