import nltk
from nltk.corpus import brown
from nltk import word_tokenize
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

raw = 'I do not like purple eggs and flower，and I also do not like her.'
tokens = word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print(default_tagger.tag(tokens))
print("The probability of correctly marking is：")
print(default_tagger.evaluate(brown_tagged_sents))
