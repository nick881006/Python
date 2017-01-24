re = iter(range(5))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ',i
    
print 'Hahaha'

#try:
#   ...
#except exception1:
#   ...
#except exception2:
#    ...
#except:
#   ...
#else:
#   ...
#finally:
#   ...

#try->异常->except->finally
#try->无异常->else->finally