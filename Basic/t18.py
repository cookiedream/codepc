while True:
    try:
        a = input()
        dic = "~!@#$%^&*()_++`1234567890-==qwertyuiop{}||[]\\\\asdfghjkl:\"\";''zxcvbnm<>??,.//"
        a = a.lower()
        for i in range (len(a)):
            for j in range(len(dic)):
                if a[i]==dic[j] :
                    print(dic[j+1],end='')
                    break
        print()
    except:
        break