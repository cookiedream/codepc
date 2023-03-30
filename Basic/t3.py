while True:
    try :
        x,y=map(int,input().split())
        circle = 100*100
        inputpoint = x*x + y*y
        if circle>=inputpoint:
            print("inside")
        else:
            print("outside")
    except:
        break