dic = {'tom':11,'nick':28,'sam':19}
print type(dic)
print dic['tom']
dic['micky']=100
print dic

for key in dic:
    print dic[key]
    
print dic.keys()
print dic.values()
print dic.items()

del dic['tom']
print dic.items()

print len(dic)