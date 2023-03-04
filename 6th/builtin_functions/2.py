def hey(d):
    if(d.isascii() == True):
        cnt1 = 0
        cnt2 = 0
        for i in d:
            if(i.isupper()==True):
                cnt1+=1
            elif(i.islower()==True):
                cnt2+=1
    
    print("The number of lowercase letters is equal to: ", cnt2)
    print("The number of uppercase letters is equal to: ", cnt1)      
    
    
hey("Hello")