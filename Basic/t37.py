while True:
    try:
        a = [0]*4
        count = [0]*6
        for i in range(4):
            a[i]=int(input())
            for j in range (6):
                if a[i]==j+1:
                    count[j]+= 1
        temp =[]
        one =0
        for i in range(6):
            if count[i]==4:
                print("WIN")
                break
            elif count[i]==3:
                print("R")
                break
            elif count[i]==2:
                temp += [i+1]
            elif count[i]==1:
                one+=1
        total = 0    
        if len(temp)==2:
            if temp[0]>temp[1]:
                print(temp[0]*2)
            else:
                print(temp[1]*2)
        elif len(temp)==1 and temp[0]!=0:
            for j in range (4):
                if a[j]!= temp[0]:
                    total += a[j]
            print(total)
        elif one==4:
            print("R")
    except:
        break