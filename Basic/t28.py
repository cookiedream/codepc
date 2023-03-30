while True:
    try:
        awd = [0]*4
        for i in range (4):
            awd[i] = input()
        n = int(input())
        count = [0]*7
        s = 0        
        for i in range (n):
            num = input()
            if num == awd[0]:
                count[0] = count[0]+1
                s = s + 2000000
            else:
                for j in range(1,4):
                    if num == awd[j]:
                        count[1] = count[1]+1
                        s = s + 200000
                    elif num[1:] == awd[j][1:]:
                        count[2] = count[2]+1
                        s = s + 40000
                    elif num[2:] == awd[j][2:]:
                        count[3] = count[3]+1
                        s = s + 10000
                    elif num[3:] == awd[j][3:]:
                        count[4] = count[4]+1
                        s = s + 4000
                    elif num[4:] == awd[j][4:]:
                        count[5] = count[5]+1
                        s = s + 1000
                    elif num[5:] == awd[j][5:]:
                        count[6] = count[6]+1
                        s = s + 200
        for i in range(7):
            if i!=6:
                print(count[i],end=" ")
            else:
                print(count[i])
        print(s)
    except:
        break