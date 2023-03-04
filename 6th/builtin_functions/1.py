def ok(q):
    k = 1
    for i in q:
        k = k*i
    print(k)
    
 
if(callable(ok)):
    print("Here we go")
    ok([2, 6, 5])
    ok([1,2,3,4,5,6])
