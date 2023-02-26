def mf(n):
    cnt = 1
    while cnt<n+1:
        yield cnt**2
        cnt+=1
        
for i in mf(4):
    print(i)