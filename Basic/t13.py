while True:
    try:
        n = int(input())
        for i in range (0,n):
            a =[str(j) for j in input().split()]
            l = len(a)
            dic = {'S':4,'H':3,'D':2,'C':1}   
            i = 1
            while (i<l):
                if(dic[a[i-1][0]]<dic[a[i][0]]):
                    a[i-1],a[i] =a[i],a[i-1]
                    i = 0
                i = i+1
            i = 1
            while (i<l):
                if(a[i-1][0]==a[i][0]):
                    if(int(a[i-1][1:])<int(a[i][1:])):
                        a[i-1],a[i] = a[i],a[i-1]
                        i = 0
                i = i+1
            for i in range (0,l):
                for j in range (0,len(a[i])):
                    print(a[i][j],end = '')
                print(end = ' ')
            print()
    except:
        break