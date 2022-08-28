import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

fd = nltk.FreqDist(brown.words(categories = 'news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories = 'news'))
most_freq_words = fd.most_common(100)

print("Most Frequent Words Top100: ")
print(most_freq_words)

likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model = likely_tags)
print("The accuracy is：")
print(baseline_tagger.evaluate(brown_tagged_sents))
