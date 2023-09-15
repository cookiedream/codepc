#include <cstdio>
#include <cstring>

const int N = 1e6 + 5;  // 定義一個常數N，代表範圍的上界

int tot, p[N];          // tot用於計數質數，p[N]用於儲存質數
bool flg[N], vis[N];    // flg[N]和vis[N]是布林陣列，用於標記數字是否為質數或是否被訪問過

void init() {
    for (int i = 2; i < N; ++i) {  // 初始化函數，找出2到N-1之間的所有質數
        if (!flg[i]) p[++tot] = i;  // 如果i是質數，將其加入p陣列，並增加tot計數
        for (int j = 1; j <= tot && i * p[j] < N; ++j) {  // 遍歷已知的質數
            flg[i * p[j]] = 1;      // 標記i*p[j]為非質數
            if (i % p[j] == 0) break;  // 如果i能被p[j]整除，跳出迴圈
        }
    }
}

void chkmin(long long &x, long long a, long long b, long long &p1, long long &p2) {
    if (x > b - a) x = b - a, p1 = a, p2 = b;  // 更新最小值和對應的數字
}

void chkmax(long long &x, long long a, long long b, long long &p1, long long &p2) {
    if (x < b - a) x = b - a, p1 = a, p2 = b;  // 更新最大值和對應的數字
}

int main() {
    init();  // 呼叫初始化函數來找出質數

    long long l, r;
    while (~scanf("%lld%lld", &l, &r)) {  // 不斷讀取輸入範圍l和r
        memset(vis, 1, sizeof(vis));  // 使用memset初始化vis陣列為全1，表示所有數字都未訪問過
        if (l == 1) vis[0] = 0;  // 如果l等於1，將vis[0]設置為0，表示1不是質數

        for (int i = 1; i <= tot; ++i) {
            for (long long j = l / p[i]; j * p[i] <= r; ++j) {
                long long x = p[i] * j;
                if (j > 1 && x >= l) vis[x - l] = 0;  // 根據質數p[i]的倍數標記非質數
            }
        }

        long long p = 0, p1, p2, p3, p4, mn = 1LL << 60, mx = 0;  // 初始化變數

        for (long long i = l; i <= r; ++i) {
            if (!vis[i - l]) continue;  // 如果i不是質數，繼續下一個數字
            if (p) chkmin(mn, p, i, p1, p2), chkmax(mx, p, i, p3, p4);  // 更新最小和最大距離
            p = i;  // 更新p為當前數字i
        }

        if (!mx) puts("There are no adjacent primes.");  // 如果最大距離為0，輸出提示信息
        else printf("%lld,%lld are closest, %lld,%lld are most distant.\n", p1, p2, p3, p4);  // 否則輸出最近和最遠的質數及其距離
    }
    return 0;
}