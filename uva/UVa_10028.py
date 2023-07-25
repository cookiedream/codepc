import sys
x=int(input())


for i in range(x):
    demerit=0
    
    while True:
        n1=input()
        total=0
        if n1== "":
            while True:
                if merit>=5:
                    sys.exit()
                elif(demerit-demerit/2)>=2:
                    year=year+1
                    demerit=demerit/2
                    print("%s-%s-%s %d demerit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(demerit)))    
                elif demerit==0:
                    year=year+2
                    merit=merit+1
                    print("%s-%s-%s %d merit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(merit)))
                    
                else:
                    year=year+1
                    print("%s-%s-%s No merit or demerit points."%((year),(str(month).zfill(2)),(str(date).zfill(2))))
                    demerit=0
                    merit=0
                
        elif len(n1)==8:
            print("%s-%s-%s No merit or demerit points."%((n1[0:4]),(n1[4:6]),(n1[6:8])))
            demerit=0
            merit=0
            year=int(n1[0:4])
            month=int(n1[4:6])
            date=int(n1[6:8])
        else :
            
            year1=int(n1[0:4])
            month1=int(n1[4:6])
            date1=int(n1[6:8])
            total=int(year1-year)
            
            if (total)>=2 :
                
                if demerit>0 and merit==0:
                    
                    for i in range(i,total):
                        year=year+1
                        if (demerit-demerit/2)>=2 :
                            if year1==year and (month<month1 or(month == month1 and date<date1)):
                                demerit=demerit/2
                                print("%s-%s-%s %d demerit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(demerit)))
                                demerit=demerit+int(n1[9:])
                                print("%s-%s-%s %d demerit point(s)."%((year),(n1[4:6]),(n1[6:8]),(demerit)))
                            elif (demerit-demerit/2)>=2:
                                demerit=demerit/2
                                print("%s-%s-%s %d demerit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(demerit)))
                            else:
                                print("%s-%s-%s No merit or demerit points."%((year),(str(month).zfill(2)),(str(date).zfill(2))))
                                demerit=0
                                merit=0
                                break
                        elif (demerit-demerit//2)>=2:
                            demerit=demerit//2
                            print("%s-%s-%s %d demerit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(int(demerit))))
                        else:
                            print("%s-%s-%s No merit or demerit pointsS."%((year),(str(month).zfill(2)),(str(date).zfill(2))))
                            demerit=0
                            merit=0
                            break
                    if year1>year or (year1==year and (month<month1 or(month == month1 and date<date1))):          
                        for i in range(0,int(total/2)):
                            year=year+2
                            if(year>year1 or (year==year1 and (month>month1 or(month == month1 and date>date1))) or merit==5):
                                break
                            else:
                                merit=merit+1
                                print("%d-%s-%s %d merit point(s)."%((year),(str(month).zfill(2)),(str(date).zfill(2)),(merit)))
                            
                        if (int(n1[9:])-merit*2)>0:
                            demerit=demerit+(int(n1[9:])-merit*2)
                            print("%s-%s-%s %d demerit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(demerit)))
                            merit=0
                            
                            
                        elif (merit-int(n1[9:])*2)==0:
                            print("%s-%s-%s No merit or demerit points."%((n1[0:4]),(n1[4:6]),(n1[6:8])))
                            demerit=0
                            merit=0
                        else:
                            merit=(merit*2-int(n1[9:]))/2
                            
                            print("%s-%s-%s %d merit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(merit)))
                            demerit=0
                        year=int(n1[0:4])
                        month=int(n1[4:6])
                        date=int(n1[6:8])
                else:
                    demerit=int(n1[9:])
                    i=0
                    for i in range(i,int(total/2)):
                        year=year+2
                        if(year>year1 or (year==year1 and (month>month1 or(month == month1 and date>date1))) or merit==5):
                                break
                        else:
                            merit=merit+1
                            print("%d-%s-%s %d merit point(s)."%((year),(n1[4:6]),(n1[6:8]),(merit)))
                       
                    if (demerit-merit*2)>0:
                        demerit=int(n1[9:])-merit*2
                        print("%s-%s-%s %d demerit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(demerit)))
                        merit=0
                        
                    elif demerit-merit*2==0:
                        print("%s-%s-%s No merit or demerit points."%((n1[0:4]),(n1[4:6]),(n1[6:8])))
                        demerit=0
                        merit=0
                    else:
                        merit=(demerit-merit)/2
                        print("%d-%s-%s %d merit point(s)."%((year),(n1[4:6]),(n1[6:8]),(-merit)))
                        demerit=0
                    year=int(n1[0:4])
                    month=int(n1[4:6])
                    date=int(n1[6:8])


            else:
                demerit=demerit+int(n1[9:])
                if merit==0:
                    print("%s-%s-%s %d demerit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(demerit)))
                elif demerit<(merit*2):
                    merit=(merit*2-demerit)/2
                    print("%s-%s-%s %d merit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(merit)))
                    demerit==0
                else:
                    demerit=demerit-merit*2
                    print("%s-%s-%s %d demerit point(s)."%((n1[0:4]),(n1[4:6]),(n1[6:8]),(demerit)))
                    merit==0
                year=int(n1[0:4])
                month=int(n1[4:6])
                date=int(n1[6:8])