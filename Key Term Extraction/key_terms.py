import string
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# getting the XML file
news = "news.xml"
root = etree.parse(news).getroot()
article = root[0]
article_head = []
article_text = []
article_counter = {}
lemmatizer = WordNetLemmatizer()
# extracting the titles and articles from XML
for i in article:
    for x in i:
        if x.get("name") == "head":
            article_head.append(x.text)
        else:
            article_text.append(x.text)
for i in range(len(article_text)):
    # tokenizing text
    tokenized = word_tokenize(article_text[i].lower())
    lem = []
    tagged = []
    for x in tokenized:
        # lemmatizing text and only keeping the nouns
        lem.append(lemmatizer.lemmatize(x, pos="n"))
    for y in lem:
        # removing unnecessary words
        if y in stopwords.words("english") or y in list(string.punctuation) or y in ['ha', 'wa', 'u', 'a']:
            while y in lem:
                lem.remove(y)
    for k in lem:
        # individually tagging each word without using context to better filter nouns
        if nltk.pos_tag([k])[0][1] == "NN":
            tagged.append(k)
    article_counter[article_head[i]] = tagged
    lem = []
    tagged = []

# creating TF-IDF matrix 
dataset = [" ".join(x for x in y) for y in article_counter.values()]
vectorizer = TfidfVectorizer(use_idf=True)
matrix = vectorizer.fit_transform(dataset)
list1 = []
vect_dict = {}
# matching the TF-IDF values from the matrix to its words and articles
for i in range(10):
    vect_dict[article_head[i]] = dict(zip(vectorizer.get_feature_names_out(), matrix.toarray()[i]))
# sorting the values inversely by TF-IDF and if values are same, sorts alphabetically 
sort_vect = {d: (sorted(k.items(), key=lambda x: (x[1], x[0]), reverse=True))
             for d, k in vect_dict.items()}
# print 5 words with the highest TF-IDF score in each article
for i in sort_vect.items():
    print(f"{i[0]}:")
    for y, x in enumerate(i[1]):
        print(x[0], end=" ")
        if y == 4:
            break
    print("\n")
