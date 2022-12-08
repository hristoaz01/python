import re
text = "hello, word of word"
chars_popularity = {}
words_popularity = {}

for i in range(int(len(text))):
    if text[i].isalpha():
        chars_popularity[text[i]] = 0
for i in range(int(len(text))):
    if text[i].isalpha():
        chars_popularity[text[i]] += 1
print(chars_popularity)
words = re.findall(r'\w+', text)

for i in range (int(len(words))):
    words_popularity[words[i]] = 0
for i in range(int(len(words))):
    words_popularity[words[i]] += 1
print (words_popularity)