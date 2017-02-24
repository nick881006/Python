# coding=utf-8
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}           # 姓名字典, 键为人物名称，值为该人物在全文中出现的次数
relationships = {}  # 关系字典, 键为有向边的起点，值为一个字典edge，edge的键是有向边的终点，值是有向边的权值，代表两个人物之间联系的紧密程度
lineName = []       # 每段内人物关系, 保存对每一段分词得到当前段中出现的人物名称

jieba.load_userdict("dict.txt")     # 加载词典
with codecs.open("busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)       # 分词并返回该词词性
        lineName.append([])         # 为新读入的一段添加人物名称列表
        # 当分词长度小于2或该词词性不为nr时认为该词
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue
            # 为当前段的环境增加一个人物
            lineName[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            # 该人物出现次数加 1
            names[w.word] += 1

for line in lineName:       # 对于每一段
    for name1 in line:
        for name2 in line:  # 每段中的任意两个人
            if name1 == name2:
                continue
            # 若两人尚未同时出现则新建项
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] += 1

with codecs.open("busan_node.txt", "w", "utf8") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

# 假设共同出现次数少于 3 次的是冗余边
with codecs.open("busan_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")