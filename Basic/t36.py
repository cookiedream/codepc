while True: # 無窮迴圈，程式會一直執行直到使用者輸入非整數的值
    try:  # 嘗試讀取使用者輸入的整數值
        year = int(input())
        if year%4==0 and year%100!=0: # 如果年份是 4 的倍數且不是 100 的倍數，或是 400 的倍數，則為閏年
            print("Bissextile Year")
        elif year%400==0:
            print("Bissextile Year")
        else : # 否則為平年
            print("Common Year") 
    except: # 如果讀取失敗（例如使用者輸入了字串），則跳出迴圈
        break