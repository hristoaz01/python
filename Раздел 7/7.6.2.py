x = 2199

roman_numeral = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
                 'CM': 900, 'M': 1000}
keys = list(roman_numeral.keys())
i = 12
while x:
    div = x // roman_numeral[keys[i]]
    x %= roman_numeral[keys[i]]
    while div:
        print(keys[i], end="")
        div -= 1
    i -= 1
