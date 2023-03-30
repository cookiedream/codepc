while True:
    try:
        string = [str(j) for j in input().split()]
        newstr = []
        for i in range (0,len(string)):
            string[i] = string[i].lower()
            if string[i] in newstr:
                continue
            else:
                newstr.append(string[i])
        for i in newstr:
            if i ==newstr[-1]:
                print(i,end = '\n')
            else:
                print(i,end = ' ')
    except:
        break