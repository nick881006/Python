#coding=utf-8
#random.choice(seq)   # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
#random.sample(seq,k) # 从序列中随机挑选k个元素
#random.shuffle(seq)  # 将序列的所有元素随机排序

#random.random()          # 随机生成下一个实数，它在[0,1)范围内。
#random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内。

#random.gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。 
#random.expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。

import random
all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
random.shuffle(all_people)
for i,name in enumerate(all_people):
    print(i,':'+name)