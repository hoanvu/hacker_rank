import re

roman = raw_input()
pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

match = re.search(pattern, roman)
if match:
    print True
else:
    print False
