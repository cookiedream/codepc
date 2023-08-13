# 定義一個函式 LCS(X, Y, m, n)，用於計算兩個序列 X 和 Y 的最長公共子序列長度。
def LCS(X, Y, m, n):
    # 創建一個二維的動態規劃表 dp，大小為 (m+1) x (n+1)，用於儲存計算結果。
    dp = [[0 for y in range(n+1)] for x in range(m+1)]

    # 使用雙重迴圈填充動態規劃表 dp。
    for i in range(m+1):
        for j in range(n+1):
            # 初始化第一行和第一列的值為 0，因為空序列的最長公共子序列長度為 0。
            if i == 0 or j == 0:
                dp[i][j] = 0
            # 若兩個序列的元素相同，則在 (i, j) 位置的最長公共子序列長度為 (i-1, j-1) 位置的長度加 1。
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # 否則，取 (i-1, j) 位置和 (i, j-1) 位置的長度的最大值填入 (i, j) 位置。
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 最終結果儲存在 dp[m][n] 中，即兩個序列的最長公共子序列長度。
    res = dp[m][n]
    return res

# 程式主體
if __name__ == '__main__':
    cnt = 0
    while True:
        # 讀取兩個整數 m 和 n，分別代表序列 A 和序列 B 的長度。
        m,n = map(int,input().split())
        cnt += 1
        # 若 m 和 n 都為 0，則結束迴圈。
        if m == 0 and n == 0:
            break
        # 讀取序列 A 和序列 B 的元素。
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        # 輸出結果，包括案例編號、最長公共子序列長度。
        print('Twin Towers #%d'%cnt)
        print('Number of Tiles : %d'%LCS(A,B,m,n))
        print()