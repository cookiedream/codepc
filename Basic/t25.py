while True:
    try:
        n = int(input())
        for i in range(n):
            a = input()
            sum = 0
            for j in range(0,len(a)):
                sum = sum + ord(a[j])
            print(sum)
    except:
        break