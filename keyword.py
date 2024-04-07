from konlpy.tag import Mecab, Okt, Kkma, Hannanum
from collections import Counter
from wordcloud import WordCloud
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

file = open('result.log', "r")
text = file.read()

okt = Okt()

result = okt.morphs(text)

result = [x for x in result if len(x) > 1]
result = [x for x in result if "\n" not in x]
result = [x for x in result if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', x)) > 0]

count = Counter(result)

list = count.most_common(100)

wordcloud = WordCloud(font_path='font/NanumGothic.ttf', \
			background_color='white', \
			width=1000, \
			height=1000, \
			max_words=100, \
			max_font_size=300)
wordcloud.generate_from_frequencies(dict(list))
wordcloud.to_file('keyword.png')
