#include<cstdio>
#include<cmath>
#include<climits>
#define N 101

struct Point
{
    double x, y;

    double getDistance(const Point& a)
    {
        return sqrt((x - a.x)*(x - a.x) + (y - a.y)*(y - a.y));
    }

}point[N];

double prim(int n);
int main()
{
    int Case;
    scanf("%d", &Case);

    int M[N][N] = {};
    while (Case--)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%lf%lf", &point[i].x, &point[i].y);

        printf("%.2lf\n", prim(n));  // 呼叫prim函式計算最小生成樹的權重總和並輸出，保留兩位小數
        if (Case)
            putchar('\n');  // 如果不是最後一個測試案例，輸出一個空行
    }

    return 0;
}

// prim演算法，計算最小生成樹的權重總和
double prim(int n)
{
    bool isVisit[N] = {}; // 標記節點是否已經加入最小生成樹
    double w[N][N] = {}, d[N]; // w陣列用來儲存點之間的距離，d陣列用來儲存每個點到最小生成樹的最短距離
    double sum = 0; // 初始化最小生成樹的權重總和為0

    //建 adjacency matrix，計算每對點之間的距離並儲存
    int i, j;
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            w[j][i] = w[i][j] = point[i].getDistance(point[j]);

    //從 0 開始走，將0點加入最小生成樹，初始化d陣列
    for (i = 0; i < n; i++)
        d[i] = w[0][i];
    isVisit[0] = true;

    for (i = 0; i < n; i++)
    {
        //找離樹最近的點，將其加入最小生成樹
        int next = -1;
        double min = INT_MAX;
        for (j = 0; j < n; j++)
            if (d[j] < min&&!isVisit[j])
            {
                min = d[j];
                next = j;
            }

        //已經沒有離樹最近的點了，退出迴圈
        if (next == -1)
            break;

        sum += min; // 將找到的最短距離加到最小生成樹的權重總和上
        isVisit[next] = true; // 將這個點標記為已訪問，加入最小生成樹

        //根據新加入的點，更新樹到各點的最短距離
        for (j = 0; j < n; j++)
            if (w[next][j] < d[j])
                d[j] = w[next][j];
    }

    return sum; // 返回最小生成樹的權重總和
}