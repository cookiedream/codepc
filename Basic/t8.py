while True:
    try:
        count = 0  # 設定計數器初始值為0
        n = int(input())  # 使用者輸入一個整數n
        for i in range(2,n):  # 對2~n-1的數字進行迴圈
            if(n%i==0):  # 如果n可以被i整除
                count = count +1  # 計數器+1
        if(count==0):  # 如果計數器仍為0，表示n只有1和n本身能夠整除，是質數
            print("YES")
        else:
            print("NO")  # 如果計數器不為0，表示n還有其他數可以整除，不是質數
    except:  # 如果有例外發生，跳出迴圈
        break
