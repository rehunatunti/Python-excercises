import datetime
import time
import locale
locale.setlocale(locale.LC_TIME, 'fi-FI')
# Nykyisen ajanhetken tulostus. srtrf()-funktion sisään voi tulostaa koko rimpsun.
# "%d" = päivä, "%B" = Kuukauden nimi, "%G" = vuosi, "%X" = kellonaika
tanaan = datetime.datetime.now()

print("\nPäivämäärä ja tekstianalyysi\n")
print("Tänään on", tanaan.strftime("%d. %Bta %G, %X"))
print("""
1. Päivämääräanalyysi
2. Tekstianalyysi""")

while True: 
	choice = input("\nValitse ohjelma 1 tai 2. Pelkkä enter lopettaa ohjelman :")
	if choice == "":
		break
	else: 
		if choice == "1":
			print("\nValitsit päivämääräanalyysin\n")
			from datetime import date
			try:
				# poimitaan päivämäärä inputista split()-metodilla
				pvmOsat = input("Anna päivämäärä muodossa pp.kk.vvvv. : ").split('.') # split() tekee item-listan
				#print(pvmOsat)
				year, month, day = [int(item) for item in pvmOsat]
				paivamaara = date(day, month, year) 
				print("Päivämäärä on ", paivamaara.strftime("%d.%m.%Y"))
				print("Viikonpäivä on", paivamaara.strftime("%w, %A.")) # %w = viikonpäivän numero, 
				print("Viikkonumero on", paivamaara.strftime("%W.")) # %W = viikkonumerot, ma on viikon 1. pvä
				print("Kuukausi on", paivamaara.strftime("%B."))
				# Karkausvuoden tarkistaminen jakojäännösten avulla. Karkausvuoden oltava jaollinen 400 ja 4:llä.
				# Mikä on y % 100 != 0?
				y = paivamaara.year
				if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
					print("Tämä vuosi on karkausvuosi.")
				else:
					print("Tämä vuosi ei ole karkausvuosi.")
			except: 
				print("Väärä syöte.") # Tämä virheentarkistus vie alku"valikkoon"

		elif choice == "2":
			print("\nValitsit tekstianalyysin\n")
			import re

			while True:
				sample = input("""Kirjoita/kopioi teksti tähän (pelkkä enter palauttaa alkuun):""")
				if sample == "":
					break
				else:
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

		else:
			print("Väärä syöte")