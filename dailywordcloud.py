import jieba
import wordcloud

w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',height=700,max_words=100,)

f = open("G:\python\daily.txt","rb")
text = f.read()
f.close()

words = jieba.lcut(text)  #分割成词语
w.generate(' '.join(words)) #空格隔开并赋给词云w

w.to_file('G:\python\daily.png')

words = jieba.lcut(text)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(300):
    word,count = items[i]
    print("{:<10}{:<10}".format(word,count))