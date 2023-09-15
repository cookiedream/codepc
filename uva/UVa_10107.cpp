#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;  

int main()
{
    int n = 1;        // 設定整數 n 為 1，用來表示數組中的元素個數
    int a[10000];     // 創建一個大小為 10000 的整數數組 a

    // 使用 while 迴圈不斷讀取輸入，直到無法讀取為止
    while (scanf("%d", &a[n]) == 1) {
        sort(a, a + n + 1);    // 對數組 a 中的元素進行排序，排序範圍是從 a[0] 到 a[n]

        if (n == 1) {
            printf("%d\n", a[1]);   // 如果數組中只有一個元素，則直接輸出該元素
        } else if (n % 2 == 0) {
            printf("%d\n", (a[n / 2] + a[(n / 2) + 1]) / 2);   // 如果數組元素個數是偶數，計算中位數並輸出
        } else if (n % 2 != 0) {
            printf("%d\n", a[(n / 2) + 1]);   // 如果數組元素個數是奇數，直接輸出中間位置的元素作為中位數
        }
        n++;   // 增加數組中的元素個數
    }
    return 0;   // 程式執行完畢，返回 0 表示成功
}



// input:          {1,2,3,4,50,60,70}
// 1
// 3
// 4
// 60
// 70
// 50
// 2