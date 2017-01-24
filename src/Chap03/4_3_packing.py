def func(*name):
    print type(name)
    print name

func(1,4,5)
func(2,5,6,10,11)

def func2(**dicti):
    print type(dicti)
    print dicti
    
func2(a=1,b=4)
func2(m=2,n=5,p=6,q=10)