while True:
    try:
        num = int(input())
        for i in range(num):
            result = 'F'
            grade = [int(j) for j in input().split()]
            p = 0
            for k in range(3):
                if(grade[k]>=60):
                    p += 1
            if p == 3:
                result = 'P'
            elif p == 2 and sum(grade)>=220:
                result = 'P'
            elif p == 2 and sum(grade)<220:
                result = 'M'
            elif p == 1:
                for j in range(3):
                    if grade[j]>=80:
                        result = 'M'
                        break
            print(result)        
    except:
        break