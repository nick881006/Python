#coding=utf-8
from itertools import imap,ifilter,groupby

rlt = imap(pow, [1, 2, 3], [1, 2, 3])
for num in rlt:
    print(num)
    
test2 = ifilter(lambda x: x > 5, [2, 3, 5, 6, 7]) #将lambda函数依次作用于每个元素，如果函数返回True，则收集原来的元素。6, 7。
for test1 in test2:
    print test1
    
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))