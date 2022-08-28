import nltk
from nltk.corpus import brown

brown_all_tagged = brown.tagged_words(tagset='universal')
AdjList = []
count = 0
for (word, tag) in brown_all_tagged :
    if tag == 'ADJ':
        AdjList.append(word)
        count += 1
    if count >= 10:
        break

allList = nltk.FreqDist(word for (word, tag) in brown_all_tagged if tag == 'ADJ')

print("The frequency of Top 10 words tagged ADJ are:")
for adj in AdjList:
    print(adj + ': ', allList[adj] / allList.__len__())
