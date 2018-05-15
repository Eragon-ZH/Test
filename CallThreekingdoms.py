#CallThreekingdoms.py
#  -*- coding:utf8 -*-
import jieba 

text = open("threekingdoms.txt","rb").read()
words = jieba.lcut(text)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print("{:<10}{:<10}".format(word,count))
