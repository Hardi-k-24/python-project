from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words=set(stopwords.words("english"))
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_sent=word_tokenize(text)
filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_sent)
print()
print()
print("Filterd Sentence:",filtered_sent)