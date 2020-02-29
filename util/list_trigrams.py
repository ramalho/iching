import unicodedata

FIRST_TRIGRAM_CODE = 0x2630

for i in range(8):
    char = chr(FIRST_TRIGRAM_CODE + i)
    name = unicodedata.name(char).split()[-1]
    print(f'    {name!r:10}: (7, 7, 7),  # {char}')
