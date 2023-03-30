while True:
    try:
        num = [str(j) for j in input().split()]
        temp = [0]*len(num)
        count = [0]*len(num)
        ind = 0
        for i in range(len(num)):
            for j in range(len(temp)):
                if (num[i] == temp[j]):
                    count[j] += 1
                    break
            if num[i] not in temp:
                temp[ind] = num[i]
                count[ind] += 1 
                ind += 1
        for i in range(len(temp)):
            if count[i]>(len(num)/2):
                print(temp[i])
                break
            elif i == len(num)-1:
                print("NO")           
    except:
        break