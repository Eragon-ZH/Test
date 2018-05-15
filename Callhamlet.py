#Callhamlet.py

def getText():
    text = open("hamlet.txt","r").read()
    text = text.lower()
    for ch in '''~!@#$%^&*()_+{}[]|\:";,./<>?/*-+-=`''':
        text = text.replace(ch," ")
    return text

hamletText = getText()
words = hamletText.split()
count = {}
for word in words:
    count[word] = count.get(word,0) + 1
items = list(count.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word,count = items[i]
    print("{:<10}{:<10}".format(word,count))
