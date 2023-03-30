while True:
    try:
        month,day = map(int,input().split())
        if (month == 1 and day > 20)or(month == 2 and day < 19):
            print("Aquarius")
        elif (month == 2 and day > 18)or(month == 3 and day < 21):
            print("Pisces")
        elif (month == 3 and day > 20)or(month == 4 and day < 21):
            print("Aries")
        elif (month == 4 and day > 20)or(month == 5 and day < 22):
            print("Taurus")
        elif (month == 5 and day > 21)or(month == 6 and day < 22):
            print("Gemini")
        elif (month == 6 and day > 21)or(month == 7 and day < 23):
            print("Cancer")
        elif (month == 7 and day > 22)or(month == 8 and day < 24):
            print("Leo")
        elif (month == 8 and day > 23)or(month == 9 and day < 24):
            print("Virgo")
        elif (month == 9 and day > 23)or(month == 10 and day < 24):
            print("Libra")
        elif (month == 10 and day > 23)or(month == 11 and day < 23):
            print("Scorpio")
        elif (month == 11 and day > 22)or(month == 12 and day < 22):
            print("Sagittarius")
        elif (month == 12 and day > 21)or(month == 1 and day < 21):
            print("Capricorn")
    except:
        break