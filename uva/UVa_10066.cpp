#include <iostream>
#include <cstdio>
#include <algorithm>

#define MAX 120

using namespace std;

int main(void) {
    int N1, N2, T = 1;
    int tower1[MAX], tower2[MAX];

    // 進入 while 迴圈，讀取兩個塔的高度 N1 和 N2，並確保兩者不為零
    while (scanf("%d %d", &N1, &N2) != EOF && (N1 | N2)) {
        int tiles[MAX][MAX];

        // 讀取塔1的高度序列
        for (int i = 1; i <= N1; ++i)
            scanf("%d", &tower1[i]);

        // 讀取塔2的高度序列
        for (int i = 1; i <= N2; ++i)
            scanf("%d", &tower2[i]);

        // 初始化動態規劃表
        for (int i = 0; i <= N1; ++i)
            tiles[i][0] = 0;
        for (int j = 0; j <= N2; ++j)
            tiles[0][j] = 0;

        // 開始計算最長共同子序列的長度（LCS）
        for (int i = 1; i <= N1; ++i) {
            for (int j = 1; j <= N2; ++j) {
                if (tower1[i] == tower2[j])
                    tiles[i][j] = tiles[i - 1][j - 1] + 1; // 如果兩個塔的高度相同，則 LCS 長度加1
                else
                    tiles[i][j] = max(tiles[i - 1][j], tiles[i][j - 1]); // 否則選擇上一行或上一列的較大值
            }
        }

        // 輸出結果
        printf("Twin Towers #%d\n", T++);
        printf("Number of Tiles : %d\n\n", tiles[N1][N2]);
    }

    return 0;
}
