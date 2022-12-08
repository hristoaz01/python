book = {'Maxim': '546789', 'Alina': '485135'}
book_keys = list(book.keys())
book_new = {}
for i in range(len(book)):
    book_new[book[book_keys[i]]] = book_keys[i]
print(book_new)operator.itemgetter(1)))