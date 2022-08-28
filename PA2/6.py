import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories = 'news')
brown_sents = brown.sents(categories = 'news')
size = int(len(brown_tagged_sents)* 0.5)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007])
unseen_sent = brown_sents[4203]

print("Label the sentence using bigram:")
print(bigram_tagger.tag(unseen_sent))
print("The accuracy is：")
print(bigram_tagger.evaluate(test_sents))
