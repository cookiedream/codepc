#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

// 定義點的結構
struct Point {
    int group;  // 群組標記，用來協助建立最小生成樹
    double x;   // x 座標
    double y;   // y 座標
};

// 定義邊的結構
struct Line {
    int aPointIndex;    // 第一個點的索引
    int bPointIndex;    // 第二個點的索引
    double length;      // 邊的長度
};

// 比較函式，用來對邊按照長度進行排序
bool compareByLength(const Line &a, const Line &b) {
    return a.length < b.length;
}

// 計算兩點之間的歐氏距離
double pointDistance(const Point &a, const Point &b) {
    double deltaX = a.x - b.x, deltaY = a.y - b.y;
    return sqrt(deltaX * deltaX + deltaY * deltaY);
}

// 檢查是否已經建立完成最小生成樹
bool isBuildMSTFinished(const Point points[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        if (points[i].group != points[i + 1].group) {
            return false;
        }
    }
    return true;
}

// 將兩個群組中的點合併成一個群組
void putInSameGroup(Point points[], int n, int group1, int group2) {
    int minGroup = min(group1, group2);
    for (int i = 0; i < n; ++i) {
        if (points[i].group == group1 || points[i].group == group2) {
            points[i].group = minGroup;
        }
    }
}

int main() {
    int test;
    while (scanf("%d", &test) != EOF) {   // 讀取測試案例數
        for (int caseCount = 0; caseCount < test; ++caseCount) {
            if (caseCount > 0) printf("\n"); // 測試案例之間輸出空行

            int n;
            scanf("%d", &n);    // 讀取點的數量

            Point points[105];
            for (int i = 0; i < n; ++i) {
                scanf("%lf%lf", &(points[i].x), &(points[i].y)); // 讀取每個點的座標
                points[i].group = i;    // 初始化每個點的群組標記
            }

            vector<Line> lines;
            // 生成所有可能的邊，並計算每條邊的長度，將其存入 lines 向量
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    Line l;
                    l.aPointIndex = i;
                    l.bPointIndex = j;
                    l.length = pointDistance(points[i], points[j]);
                    lines.push_back(l);
                }
            }

            sort(lines.begin(), lines.end(), compareByLength); // 將邊按照長度進行排序

            double pathLengthSum = 0;
            for (int i = 0; !isBuildMSTFinished(points, n); ++i) {
                if (points[lines[i].aPointIndex].group == points[lines[i].bPointIndex].group) {
                    continue;   // 若邊的兩端點屬於同一群組，則忽略該邊，以避免形成環路
                }
                pathLengthSum += lines[i].length;   // 加入該邊的長度到總權重中
                putInSameGroup(points, n, points[lines[i].aPointIndex].group, points[lines[i].bPointIndex].group);
                // 將兩端點所屬群組合併成一個群組
            }

            printf("%.2lf\n", pathLengthSum); // 輸出最小生成樹的總權重，並保留兩位小數
        }
    }
    return 0;
}