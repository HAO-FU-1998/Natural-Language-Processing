import nltk
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can','could','may','might','must','will','what','when','where','who','why']
for m in modals:
    print(m + ':', fdist[m]/len(news_text), end=' ')

print("==============================================")
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can','could','may','might','must','will','what','when','where','who','why']
cfd.tabulate(conditions=genres, samples=modals)
