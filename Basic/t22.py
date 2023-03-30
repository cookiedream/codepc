while True:
    try:
        game = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            a = [int(j) for j in input().split()]
            game[i][0] = a[0]
            game[i][1] = a[1]
            game[i][2] = a[2]
        result = False
        for i in range(3):
            if game[i][0]==game[i][1] and game[i][1]==game[i][2]:
                result = True
            elif game[0][i]==game[1][i] and game[1][i]==game[2][i]:
                result = True
        if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
            result = True
        elif game[2][0]==game[1][1] and game[1][1]==game[0][2]:
            result = True
        print(result)
    except:
        break