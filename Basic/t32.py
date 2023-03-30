while True:
    try:
        text = input()
        n = int(input())
        for i in range (len(text)):
            shift = 0
            if 90>=ord(text[i])>=65: ##處理大寫英文字
                shift = ord(text[i]) + n
                if shift>90: ##如果超過Z就回到A繼續
                    shift -= 26
            elif 122>=ord(text[i])>=97: ##處理小寫英文字
                shift = ord(text[i]) + n
                if shift>122: ##如果超過z就回到a繼續
                    shift -= 26
            elif 57>=ord(text[i])>=48: ##處理數字
                shift = ord(text[i]) + n
                if shift>57: ##如果超過9就回到0繼續
                    shift -= 10
            else: ##除了大小寫英文字與數字之外，其他字元不動
                shift = ord(text[i])
            if i == len(text)-1:
                print(chr(shift))
            else:
                print(chr(shift),end='')
    except:
        break