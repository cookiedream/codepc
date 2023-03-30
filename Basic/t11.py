while True:
    try:
        n,m = map(int,input().split())  # 讀取輸入的數字 n, m，並將其轉換為整數
        arr = []   # 創建一個空的二維列表，列表中包含 m 個空的一維列表
        for i in range(m):
            arr.append([]) 
              # 逐行讀取 n 行輸入，每行輸入包含 m 個數字，並將它們添加到 arr 中
        for i in range(n):
            # 讀取每行輸入，並將其轉換為整數列表
            a = [int(j) for j in input().split()] 
              # 將每行輸入的元素添加到對應的 arr 列表中
            for k in range(m): 
                arr[k].append(a[k]) 
                # 輸出 arr，逐行輸出每個元素，每行末尾添加一個空格
        for i in arr:
            for j in range(n):
                print(i[j] , end='') 
            print()
            # 如果輸入結束，跳出迴圈
    except:
        break