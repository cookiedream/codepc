#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>

using namespace std;
#define MAXN 100000

int pr[MAXN]; // 定義一個陣列pr，用來存儲集合的父節點，這個陣列在Union-Find算法中使用

// Union-Find算法的Find操作，用於找到節點r所屬的集合代表節點
int findset(int r)
{
    if(pr[r] == r) return r; // 如果節點r是集合的代表節點，則返回r

    return findset(pr[r]); // 否則遞迴地尋找r所在的集合代表節點
}

// Union-Find算法的MakeSet操作，用於初始化n個節點的集合
void makeset(int n)
{
    for(int i = 0; i < n; i++)
        pr[i] = i; // 初始時每個節點自成一個集合，並將其父節點設置為自身
}

// 定義邊的結構體，包含起點u、終點v和權重w
struct Edge
{
    int u, v; // 起點和終點
    double w; // 權重
    bool operator < (const Edge &p) const
    {
        return w < p.w; // 用於對邊按照權重進行遞增排序
    }
};

vector<Edge> e; // 存儲所有的邊

double dist[100][2]; // 存儲點的座標

// Kruskal演算法，用於計算最小生成樹的權重和
double krushkal(int n)
{
    double sum = 0; // 初始化最小生成樹的權重總和為0
    sort(e.begin(), e.end()); // 將所有邊按照權重進行排序
    makeset(n); // 初始化n個節點的集合
    for(int i = 0; i < (int)e.size(); i++)
    {
        int u = findset(e[i].u); // 找到邊的起點u所屬的集合代表節點
        int v = findset(e[i].v); // 找到邊的終點v所屬的集合代表節點

        if(u != v) // 如果起點和終點不在同一個集合中（不會形成環路）
        {
            pr[u] = v; // 將起點所屬的集合合併到終點所屬的集合中（使用Union操作）
            sum += e[i].w; // 將這條邊的權重加到最小生成樹的權重總和上
        }
    }
    return sum; // 返回最小生成樹的權重總和
}

int main()
{
    int kase, n, k; // 定義變數
    while(scanf("%d", &kase) == 1) // 讀取kase的值，用於控制測試案例數
    {
        while(kase--) // 開始測試案例迴圈
        {
            cin >> n; // 讀取點的個數n
            for(int i = 0; i < n; i++)
            {
                scanf("%lf %lf", &dist[i][0], &dist[i][1]); // 讀取每個點的座標
            }
            e.clear(); // 清空存儲邊的向量
            for(int i = 0; i < n; i++)
                for(int j = i + 1; j < n; j++)
                {
                    Edge data;
                    data.u = i; // 邊的起點
                    data.v = j; // 邊的終點
                    data.w = sqrt(pow(dist[i][0] - dist[j][0], 2) + pow(dist[i][1] - dist[j][1], 2)); // 計算邊的權重（歐幾里德距離）
                    e.push_back(data); // 將邊加入存儲邊的向量中
                }

            printf("%.2lf\n", krushkal(n)); // 計算最小生成樹的權重總和並輸出（保留兩位小數）
            if(kase) printf("\n"); // 如果不是最後一個測試案例，輸出一個空行
        }
    }
}