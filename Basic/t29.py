while True:
    try:
        al = "ABCDEFGHJKLMNPQRSTUVXYWZIO"
        idnum = input()
        for i in range(26):
            if idnum[0]==al[i]:
                x1 = (10+i)//10
                x2 = (10+i)%10
                break
        p = x1+(9*x2)
        for i in range(1,10):
            if i<=7:
                p = p+(9-i)*int(idnum[i])
            else:
                p = p+int(idnum[i])
        if p%10==0:
            print("CORRECT!!!")
        else:
            print("WRONG!!!")
    except:
        break