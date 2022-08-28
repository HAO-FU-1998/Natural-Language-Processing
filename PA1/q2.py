import nltk,re,pprint
from nltk import word_tokenize

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print("raw[153:175]"+raw[153:175])
print("raw[153:177]"+raw[153:177])
print("=============================================")

num1=raw.find("PART I")
num2=raw.rfind("PART II")
raw = raw[num1:num2]
print("The number is ")
print(len(raw))
