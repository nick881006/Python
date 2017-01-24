#coding=utf-8

# s为一个序列list,tuple
#len(s)         返回： 序列中包含元素的个数
#min(s)         返回： 序列中最小的元素
#max(s)         返回： 序列中最大的元素
#all(s)         返回： True, 如果所有元素都为True的话
#any(s)         返回： True, 如果任一元素为True的话
#sum(s)         返回：序列中所有元素的和
# x为元素值，i为下标(元素在序列中的位置)
#s.count(x)     返回： x在s中出现的次数
#s.index(x)     返回： x在s中第一次出现的下标

# l为一个表list, l2为另一个表list
#l.extend(l2)        在表l的末尾添加表l2的所有元素
#l.append(x)         在l的末尾附加x元素
#l.sort()            对l中的元素排序
#l.reverse()         将l中的元素逆序
#l.pop()             返回：表l的最后一个元素，并在表l中删除该元素
#del l[i]            删除该元素

#str为一个字符串，sub为str的一个子字符串。s为一个序列，它的元素都是字符串。width为一个整数，用于说明新生成字符串的宽度。
#str.count(sub)       返回：sub在str中出现的次数
#str.find(sub)        返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.index(sub)       返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.rfind(sub)       返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.rindex(sub)      返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.isalnum()        返回：True， 如果所有的字符都是字母或数字
#str.isalpha()        返回：True，如果所有的字符都是字母
#str.isdigit()        返回：True，如果所有的字符都是数字
#str.istitle()        返回：True，如果所有的词的首字母都是大写
#str.isspace()        返回：True，如果所有的字符都是空格
#str.islower()        返回：True，如果所有的字符都是小写字母
#str.isupper()        返回：True，如果所有的字符都是大写字母
#str.split([sep, [max]])    返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
#str.rsplit([sep, [max]])   返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符
#str.join(s)                返回：将s中的元素，以str为分割符，合并成为一个字符串。
#str.strip([sub])           返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub  
#str.replace(sub, new_sub)  返回：用一个新的字符串new_sub替换str中的sub
#str.capitalize()           返回：将str第一个字母大写
#str.lower()                返回：将str全部字母改为小写
#str.upper()                返回：将str全部字母改为大写
#str.swapcase()             返回：将str大写字母改为小写，小写改为大写
#str.title()                返回：将str的每个词(以空格分隔)的首字母大写
#str.center(width)          返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。
#str.ljust(width)           返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。
#str.rjust(width)           返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格 。