while True:
    try:
        a = [int(j) for j in input().split()]
        size = len(a)
        total = 0
        for i in range(len(a)):
            total += a[i]
        average = total/size
        print("Size: {}".format(size))
        print("Average: {}".format(format(average,'.3f')))
    except:
        break