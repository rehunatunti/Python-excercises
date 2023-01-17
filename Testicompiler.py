import re

sample = input("Kirjoita/kopioi teksti tähän: ")

# Välilyönnit pitää ekskluudata erikoismerkkituloksesta
x = sample.replace(" ", "")
spchar = re.findall("\W", x)
print("Erikoismerkkejä löytyi", len(spchar), "kpl.")

from collections import Counter

strLista = sample.split(' ')

maara = Counter(len(sana) for sana in strLista)

print('Pituus  Määrä')

for pituus in range(1, max(maara.keys()) + 1): # tämän logiikka ei ole aivan selvä
    print(f'{pituus:6d} {maara.get(pituus, 0):5d}')