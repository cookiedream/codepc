while True:
    try:
        isbn = [str(j) for j in input().split()]
        num1 = [0]*10
        num2 = [0]*10
        for i in range(10):
            if i==0:
                num1[i]=int(isbn[i])
            elif isbn[i]!='X':
                num1[i]+=(num1[i-1]+int(isbn[i]))
            elif isbn[i]=='X':
                num1[i]+=(num1[i-1]+10)
        for i in range(10):
            if i==0:
                num2[i]=num1[0]
            else:
                num2[i]+=(num2[i-1]+num1[i])
        if num2[9]%11==0:
            print("YES")
        else:
            print("NO")

    except:
        break