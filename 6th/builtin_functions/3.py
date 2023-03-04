def isPalindrome(ok):
    k = ""
    oksiu = reversed(ok)
    for i in oksiu:
        k=k+i
    
    
    print("1st:", ok)
    print("2nd:", k)
    if(ok == k):
        print("Yes, it's palindrome")
    else:
        print("Nope")
        
    

isPalindrome("aabaaas")    
print("-----------------------------------------------------------------------------------------------")
isPalindrome("kkkkkkkk")

            
            
            