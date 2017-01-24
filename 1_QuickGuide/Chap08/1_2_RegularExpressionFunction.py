import re

m = re.search('[0-9]', 'abcd4ef')
print (m.group(0))

#搜索整个字符串，直到发现符合的子字符串。
#m = re.search(pattern, string)

#从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
#m = re.match(pattern, string)  
 
#在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
#str = re.sub(pattern, replacement, string) 

#根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
#re.split()    

#根据正则表达式搜索字符串，将所有符合的子字符串放在一个表(list)中返回
#re.findall()  
