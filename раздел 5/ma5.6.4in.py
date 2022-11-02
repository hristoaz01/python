text = "How are you? Eh, ok. Low or Lower? Ohhh."
for i in range(len(text)):
    if (ord(text[i]) >=65) & (ord(text[i])<=90):
        print(text[i], end="")