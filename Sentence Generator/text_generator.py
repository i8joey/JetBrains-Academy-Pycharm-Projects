import random
from nltk.tokenize import WhitespaceTokenizer
import nltk


# Create a trigram from file
file = open(input(), "r", encoding="utf-8")
book = file.read()
file.close()
token_list = WhitespaceTokenizer().tokenize(book)
trigram = list(nltk.trigrams(book.split()))


# Create a dictionary with heads and tails, heads being first 2 words and the tail being the 3rd
head_dict = {}
for x in trigram:
    head = f"{x[0]} {x[1]}"
    head_dict.setdefault(head, [])
    head_dict[head].append(x[2])


# Initialize sentence
sentence = []


# Creates a list of words to start a sentence that meet the requirements
start_words = [x for x in head_dict.keys() if x[0].isupper() and not x.endswith((".", "?", "!")) and not x.split()[0].endswith((".", "?", "!"))]
count = 0


# Loop for creating a sentence
while count < 10:
    start = random.choice(start_words)
    sentence += (start.split())
    next_word = [x for x in head_dict[start]]
    sentence.append(random.choice(next_word))
    while True:
        find = sentence[-2] + " " + sentence[-1]
        if len(sentence) > 5 and sentence[-1].endswith((".", "?", "!")):
            print(" ".join(sentence))
            count += 1
            sentence = []
            break
        try:
            # If a new sentence is started, pick another word to start new sentence
            if sentence[-1].endswith((".", "?", "!")):
                sentence.append(random.choice(start_words))
            else:
                sentence.append(random.choice(head_dict[find]))
        # If the tail doesn't exist, start a new sentence
        except KeyError:
            sentence = []
            break


