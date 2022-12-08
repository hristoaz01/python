book = {'Maxim': '546123', 'Alina': '789456'}
book_keys = list(book.keys())
book_new = {}
for i in range(len(book)):
    book_new[book[book_keys[i]]] = book_keys[i]
print(book_new)
