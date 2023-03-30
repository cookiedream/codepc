# 進入無窮迴圈
while True:
    try:  # 監聽例外
        # 讀入四個整數，用逗號分隔
        N,a1,a2,a3 = map(int,input().split(','))
        # 計算剩下的錢
        rest = N-(a1*15+a2*20+a3*30)
        # 創建一個空的列表，用於計算物品數量
        count = [0,0,0]
        # 如果剩餘的錢足夠購買商品，進行以下計算
        if rest>=0:
            # 計算可以購買 50 元物品的數量
            count[0]=rest//50
            rest = rest%50  # 更新剩餘的錢
            # 計算可以購買 5 元物品的數量
            count[1]=rest//5
            rest = rest%5  # 更新剩餘的錢
            # 計算可以購買 1 元物品的數量
            count[2]=rest//1
            # 輸出結果，使用字串格式化輸出
            print("{},{},{}".format(count[2],count[1],count[0]))
        else:
            # 如果錢不夠買任何東西，輸出 0
            print(0)
    except:
        # 當有例外發生時，跳出迴圈
        break
