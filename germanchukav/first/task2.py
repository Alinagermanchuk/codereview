'''Вивести всі слова, що містять велику букву'''


string = 'FdgdxsS hfdgfd dfsgJj'
result = []
for item in string.split():
    if any(c.isupper() for c in item):
        result.append(item)
print(result)