import string
from lxml import etree
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


news = "news.xml"
root = etree.parse(news).getroot()
article = root[0]
article_head = []
article_text = []
article_counter = {}
lemmatizer = WordNetLemmatizer()
for i in article:
    for x in i:
        if x.get("name") == "head":
            article_head.append(x.text)
        else:
            article_text.append(x.text)
for i in range(len(article_text)):
    tokenized = word_tokenize(article_text[i].lower())
    lem = []
    for x in tokenized:
        lem.append(lemmatizer.lemmatize(x, pos="n"))
    for y in lem:
        if y in stopwords.words("english") or y in list(string.punctuation):
            while y in lem:
                lem.remove(y)
    article_counter[article_head[i]] = Counter(lem).most_common(10)
    lem = []
sorted_dict = {d: (sorted(k, key=lambda x: (x[1], x[0]), reverse=True))
               for d, k in article_counter.items()}
for i in sorted_dict.items():
    print(i[0] + ":")
    for x in range(5):
        print(i[1][x][0], end=" ")
    print("\n")
