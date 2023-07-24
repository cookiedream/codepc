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