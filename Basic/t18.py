while True:
    try:
        a = input()  # 接收使用者輸入的字串
        dic = "~!@#$%^&*()_++`1234567890-==qwertyuiop{}||[]\\\\asdfghjkl:\"\";''zxcvbnm<>??,.//"  # 字元對照表
        a = a.lower()  # 將輸入的字串轉換成小寫
        for i in range(len(a)):  # 迭代輸入字串的每個字元
            for j in range(len(dic)):  # 迭代字元對照表的每個字元
                if a[i] == dic[j]:  # 判斷字元是否在字元對照表中
                    print(dic[j + 1], end="")  # 輸出對應的下一個字元
                    break  # 結束內層迴圈，繼續處理下一個輸入字元
        print()  # 輸出換行
    except:
        break  # 當發生例外時（通常是使用者中斷程式），跳出迴圈結束程式的執行
