n = int(input())
o = []
def a():
    for i in range(0,n):
        if(i%2==0):
            o.append(i)
    yield o
        
print(next(a()))