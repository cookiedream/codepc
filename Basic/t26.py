while True:
    try:
        n = int(input())
        a = [str(j) for j in input().split(' ')]
        num = [0]*n
        for i in range (n):
            for k in range (len(a[i])):
                num[i] = num[i] + int(a[i][k])
        i = 1
        while(i<n):
            if num[i]<num[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
                num[i],num[i-1]=num[i-1],num[i]
                i = 0
            elif num[i]==num[i-1] and int(a[i])<int(a[i-1]):
                a[i],a[i-1]=a[i-1],a[i]
                i = 0
            i = i+1
        for i in range(n):
            print(a[i],end=" ")
        print()
    except:
        break