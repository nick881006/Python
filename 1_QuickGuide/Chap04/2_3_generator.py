def gen():
    a=100
    yield a
    a = a*3
    yield a
    yield 10000
    
for i in gen():
    print i