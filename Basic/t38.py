# 進入無窮迴圈
while True:
    # 使用者輸入一個數字
    try:
        n = int(input())
        # 初始化夏季和非夏季用電度數
        summer = 0
        nonsummer = 0
        # 如果用電度數大於 700，則計算夏季和非夏季用電費用，用電度數降至 700 往下計算
        if n > 700:
            summer += ((n - 700) * 5.63)
            nonsummer += ((n - 700) * 4.5)
            n = 700
        # 如果用電度數大於 500，則計算夏季和非夏季用電費用，用電度數降至 500 往下計算
        if n > 500:
            summer += ((n - 500) * 4.97)
            nonsummer += ((n - 500) * 4.01)
            n = 500
        # 如果用電度數大於 330，則計算夏季和非夏季用電費用，用電度數降至 330 往下計算
        if n > 330:
            summer += ((n - 330) * 4.39)
            nonsummer += ((n - 330) * 3.61)
            n = 330
        # 如果用電度數大於 120，則計算夏季和非夏季用電費用，用電度數降至 120 往下計算
        if n > 120:
            summer += ((n - 120) * 3.02)
            nonsummer += ((n - 120) * 2.68)
            n = 120
        # 如果用電度數大於 0，則計算夏季和非夏季用電費用
        if n > 0:
            summer += (n * 2.1)
            nonsummer += (n * 2.1)
        # 輸出夏季和非夏季用電費用
        print("Summer months:{}".format(format(summer,'.2f')))
        print("Non-Summer months:{}".format(format(nonsummer,'.2f')))
    # 如果使用者沒有輸入數字，則跳出迴圈
    except:
        break
