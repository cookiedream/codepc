while True:
    try:
        search = [str(j) for j in input().split()]
        string = [str(i) for i in input().split()]
        index = 0
        count = 0
        i = 0
        while(i<len(string[0])):
            if search[0][index]==string[0][i]:
                index = index+1
                if index==len(search[0]):
                    count = count +1
                    i = i - index + 1
                    index = 0
            elif index!=0:
                i = i - index
                index = 0
            i = i + 1
        print(count)    
    except:
        break