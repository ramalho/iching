import unicodedata
import sys

for code in range(sys.maxunicode+1):
    char = chr(code)
    name = unicodedata.name(char, None)
    if name and 'TRIGRAM' in name:
        print(f'U+{code:04X}\t{char}\t{name}')
