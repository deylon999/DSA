def min_path(grid):
    n = len(grid)
    m = len(grid[0])

    dp = [[0] * m for _ in range(n)] 

    dp[0][0] = grid[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, n):
        dp[0][i] = dp[i-1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1] + grid[i][j])
    
    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    path.reverse()

    return dp[n-1][m-1], path