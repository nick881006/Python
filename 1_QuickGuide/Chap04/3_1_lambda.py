func = lambda x,y:x+y
print func(3,4)

def test(f,a,b):
    print 'test'
    print f(a,b)
    
test(func, 3, 4)

test((lambda x,y:x**2+y),6,9)