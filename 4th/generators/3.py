def mf(n):
    cnt = 0
    for i in range(0, n):
        if(i%3==0 and i%4==0):
            yield cnt
        cnt+=1
k = []         
for u in mf(25):
    k.append(u)
    
print(k)