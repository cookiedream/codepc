while True:
    try:
        a,b = map(int,input().split())
        while(b!=0):
            if (a<b):
                a,b=b,a
            if(b!=0):
                a = a%b
        print(a)
    except:
        break