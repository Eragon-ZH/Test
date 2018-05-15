#用idle打开
import jieba
import wordcloud
#读取图片作为背景
from scipy.misc import imread
mk = imread('china.jpg')

w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',height=700,max_words=100,mask=mk)

f = open("2018政府工作报告.txt","rb")
text = f.read()
f.close()

words = jieba.lcut(text)  #分割成词语
w.generate(' '.join(words)) #空格隔开并赋给词云w

w.to_file('2018政府工作报告.png')
