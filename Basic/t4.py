x,x1=map(int,input().split())
y,y1=map(int,input().split())
time = (y*60+y1) - (x*60+x1)
if time<=30:
    print("free")
elif time>30 and time<=120:
    print((time//30)*30)
elif time>120 and time<=240:
    print(120+((time-120)//30)*40)
else :
    print(120+160+((time-240)//30)*60)