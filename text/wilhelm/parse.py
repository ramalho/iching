import re
import html

FIRST_HEXAGRAM = 0x4DC0

hexagram_start_re = re.compile(r'<a name="\d{1,2}"></a>')
title_parts_re = re.compile(r'(\d{1,2})\. ([^\n]+)')

dingbats = [chr(i) for i in range(0x278A, 0x2793)]  # dingbat 1 to 9

line_re = [re.compile(regex) for regex in (
    r'(°?) ?(Six|Nine) (at|in) the beginning means:',
    r'(°?) ?(Six|Nine)  ?in t?h?e second place means:',
    r'(°?) ?(Six|Nine)  ?in the third place means[:.]',
    r'(°?) ?(Six|Nine) in the fourth place means:',
    r'(°?) ?(Six|Nine) in the fifth place means:',
    r'(°?) ?(Six|Nine) at the top means:',
)]


def capture_line(n, verse):
    hit = line_re[n-1].search(verse)
    if hit is not None:
        return hit.group(1), hit.group(2)


def main():
    with open('i.html', encoding='cp1252') as fp:
        text = fp.read()
    chapters = hexagram_start_re.split(html.unescape(text))
    for i, chapter in enumerate(chapters[1:], 1):
        verses = chapter.split('\n')
        hit = title_parts_re.search(verses[1])
        n, title = hit.groups(verses[1])
        title_wg, title_en = (s.strip() for s in title.split('/'))
        assert i == int(n)
        print('_' * 60)
        hex_char = chr(FIRST_HEXAGRAM + int(n) - 1)
        print(f'{n:2}\t{hex_char} {title_wg:16} {title_en}')
        print()
        line_matches = 0
        iter_verses = iter(verses[2:])
        while True:
            try:
                verse = next(iter_verses)
            except StopIteration:
                break
            if 'THE JUDGMENT' in verse:
                while True:
                    verse = next(iter_verses)
                    verse = next(iter_verses)
                    if verse.startswith('\t') or verse.startswith(' '*3):
                        if verse.strip():
                            print('\t> '+ verse.strip())
                        else:
                            break
                    else:
                        print()
                        break
            for n in range(1, 7):
                hit = capture_line(n, verse)
                if hit is not None:
                    governing, value = hit
                    line = 6 if value == 'Six' else 9
                    dingbat = dingbats[n-1]
                    print(f'\t{dingbat} {line} {governing}', end='')
                    line_matches += 1
                    verse = next(iter_verses)
                    print(verse)
                    while verse.startswith('\t'):
                        verse = next(iter_verses)
                        if verse.strip():
                            print('\t\t  '+verse.strip())
                        else:
                            break

        if line_matches != 6:
            raise ValueError('!!! missing line text')


if __name__ == '__main__':
    main()
