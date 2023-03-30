while True:
    try:
        n = int(input())
        a = [int(j) for j in input().split()]
        carindex = 0
        car = [0]*24*n
        i = 0
        while(i<n*2):
            tim = 0
            for j in range(a[i],a[i+1]):
                if car[carindex*24+j]!=1 :
                    tim = tim +1
            if tim == a[i+1]-a[i]:
                for k in range(a[i],a[i+1]):
                    car[carindex*24+k]=1
                carindex = 0 
            else:
                carindex = carindex +1
                i = i-2
            i = i + 2
        count = 0
        for i in range (n):
            for j in range(24):
                if car[i*24+j]==1:
                    count = count+1
                    break
        print(count)
    except:
        break