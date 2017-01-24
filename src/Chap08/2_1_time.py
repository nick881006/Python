#coding=utf-8   
import time
print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second

print('start')
time.sleep(3)     # sleep for 10 seconds
print('wake up')


st = time.gmtime()      # 返回struct_time格式的UTC时间
print st
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print st
s  = time.mktime(st)    # 将struct_time格式转换成wall clock time
print s