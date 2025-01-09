for n in range(1,101):
    flag=0    
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    
    if(flag==0):
        print(n)
    
