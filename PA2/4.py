import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print("Label the sentence using Unary annotation：")
print(unigram_tagger.tag(brown_sents[2007]))
print("The accuracy is：")
print(unigram_tagger.evaluate(brown_tagged_sents))
