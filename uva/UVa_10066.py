def LCS(X, Y, m, n):
    dp = [[0 for y in range(n+1)] for x in range(m+1)]

    # 建立一個二維的動態規劃表 dp，大小為 (m+1) x (n+1)。初始化所有元素為 0。

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 使用動態規劃填充表格 dp。如果兩個序列 X 和 Y 的元素相同，則在 (i, j) 位置的最長公共子序列長度為 (i-1, j-1) 位置的長度加 1。
    # 否則，取 (i-1, j) 位置和 (i, j-1) 位置的長度的最大值填入 (i, j) 位置。

    res = dp[m][n]
    return res

# 定義一個函式 LCS(X, Y, m, n)，其中 X 和 Y 分別是兩個序列，m 和 n 分別是 X 和 Y 的長度。

if __name__ == '__main__':
    cnt = 0
    while True:
        m,n = map(int,input().split())
        cnt += 1
        if m == 0 and n == 0:break
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        print('Twin Towers #%d'%cnt)
        print('Number of Tiles : %d'%LCS(A,B,m,n))
        print()

# 在程式主體中，使用 while 迴圈來處理多組輸入。
# 每組輸入的格式為：m n (X 的長度和 Y 的長度)，接著分別輸入 X 和 Y 的元素。
# 使用 LCS 函式計算最長公共子序列長度，並印出結果。
# 若輸入的 m 和 n 都為 0，則結束迴圈。