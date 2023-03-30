while True:
    try:
        string = [str(j) for j in input().split()]
        alp = ['a','b','c','d','e','f','g', 
                'h','i','j','k','l','m','n', 
                'o','p','q','r','s','t','u', 
                'v','w','x','y','z']
        num = []
        for i in range (26):
            num.append(0)
        for i in range (len(string)):
            string[i] = string[i].lower()
        for i in range(len(string)):
            for j in range (len(string[i])):
                for a in range(26):
                    if string[i][j]==alp[a]:
                        num[a] = num[a]+1
        print(len(string))
        for i in range(26):
            if num[i]!=0:
                print( "{}:{}".format(alp[i],num[i]))
    except:
        break