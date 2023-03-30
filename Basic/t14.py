while True:
    try:
        num = [str(j) for j in input().split()] #輸入一個未知長度的字串
        numRev = [] #建立一個空的串列
        l = len(num[0])
        for i in range(l):
            numRev.append([])
        for i in range(l):
            numRev[l-1-i]=num[0][i] #將反轉之後的字串存入
        count = 0
        for i in range(l):
            if num[0][i]==numRev[i]: #判斷每一個元素是否一樣
                count= count +1
        if l==count: 
            print("YES") #每一個元素都一樣，則輸出YES
        else:
            print("NO") #反之，則輸出NO
    except:
        break