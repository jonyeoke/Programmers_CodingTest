def solution(triangle):
    answer = 0
    
    dp = [row[:] for row in triangle]
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(0, len(triangle[i])):
            dp[i][j] = max(dp[i][j]+dp[i+1][j],dp[i][j]+dp[i+1][j+1])
            
    
    
    return dp[0][0]