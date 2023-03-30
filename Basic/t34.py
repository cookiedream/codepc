while True:                                                                                                                 
    try:                                                                                                                        
        hight,gender = map(int,input().split())                                                                                 
        if gender==1:                                                                                                              
            bmi = (hight-80)*0.7                                                                                               
        elif gender==2:                                                                                                             
            bmi = (hight-70)*0.6                                                                                                
        print(format(bmi,'.1f'))                                                                                            
    except:                                                                                                                    
        break 