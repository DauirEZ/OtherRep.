a = int(input())
b = int(input())
k = []
def mf():
    for i in range(a,b):
        k.append(i**2) 
    yield k
    

print(next(mf()))