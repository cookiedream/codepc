while True:
    try:
        r = float(input())
        n = int(input())
        p = int(input())
        sum = 0
        for i in range(n):
            sum = sum + p
            sum = sum + sum * r
        print(int(sum))
    except:
        break