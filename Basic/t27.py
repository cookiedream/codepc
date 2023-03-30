while True:  # 一直重複進行以下步驟，直到程式遇到例外或中斷
    try:  # 嘗試執行以下程式碼，如果有例外就跳到except區塊
        ans = input()  # 輸入正確的數字
        inp = input()  # 輸入猜測的數字
        while(inp!="0000"):  # 如果猜的數字不是"0000"，就繼續下去
            count_a =0  # 記錄猜測的數字有幾個數字位置正確
            count_b =0  # 記錄猜測的數字有幾個數字位置不正確但出現在正確的數字中
            for i in range(len(ans)):  # 比較正確的數字和猜測的數字的每一個位置
                if ans[i]==inp[i]:  # 如果位置相同且數字相同，就是位置和數字都正確
                    count_a = count_a +1  # 計算位置和數字都正確的數字有幾個
                for j in range(len(ans)):  # 比較正確的數字和猜測的數字的每一個位置
                    if inp[i]==ans[j] and i!=j:  # 如果數字相同但位置不同，就是數字正確但位置不正確
                        count_b = count_b+1  # 計算數字正確但位置不正確的數字有幾個
            print("{}A{}B".format(count_a,count_b))  # 輸出猜測結果
            inp = input()  # 再輸入一次猜測的數字，繼續下一輪比較
    except:  # 如果有例外發生，就跳出迴圈
        break