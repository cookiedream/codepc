while True: 
    try: 
        n = int(input()) 
        for i in range(n): 
            T,m,k = map(int,input().split()) 
            gift = [int(j) for j in input().split()] 
            x = 1 
            while x<k: 
                if gift[x-1]>gift[x]: 
                    gift[x-1],gift[x]=gift[x],gift[x-1] 
                    x = 0 
                x += 1 
            total = 0 
            for y in range (m): 
                total += gift[y] 
            if T<total: 
                print("Impossible") 
            else: 
                print(total) 
    except: 
        break 