import operator
rates = {'Otkritie': 61.85, 'Sberbank': 59.39, 'VTB': 60.1, 'Gazprombank': 60.2, 'Alpha-Bank': 60}
x = len(rates)
print(max(rates.items(), key=operator.itemgetter(1)))