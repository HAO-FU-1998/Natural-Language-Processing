import nltk
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print("The context of bought is:")
text.similar('bought')
print("The context of family is:")
text.similar('family')
print("The context of through is:")
text.similar('through')
