text = "How are you? Eh, ok. Low or Lower? Ohhh."
for i in range(len(text)):
    if text[i].isupper():
        print(text[i], end='')
