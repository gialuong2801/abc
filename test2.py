import re

sentence = "Xin chao Python! Python rat thu vi! Toi rat thich no-P"
#remove special character
str = re.sub('\W+','', sentence )

frequency = []
dict = {}

for i in set(str):
    b = str.count(i, 0, len(str))
    dict[i] = b

for i in sorted(dict, key=dict.get, reverse=True):
    frequency.append((i, dict[i]))


print(frequency)
