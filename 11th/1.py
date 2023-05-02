n = int(input())
def mf():
    i = n
    k = []
    while i>=0:
        k.append(i)
        i=i-1
    yield k
    
print(next(mf()))