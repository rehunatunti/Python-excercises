#Ari Huttunen
"""
Ohjelma pyytää käyttäjältä 3 lukua ja lajittelujärjestystä (”N” tai ”L) 
ja lajittelee luvut nousevaan järjestykseen, jos lajittelujärjestys on N 
eli Nouseva tai laskevaan järjestykseen, jos lajittelu järjestys on L eli Laskeva.

Puuttuu virheentarkistus


"""

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

luvut = []
for x in range(3):
	luku = input("Anna luku:")
	if luku.isdigit() or isfloat(luku):
		luvut.append(luku)
	else:
		print("Väärä syöte")
		exit() #Väärä syöte lopettaa ohjelman
sortOrder = input("Nouseva (N) vai laskeva (L) järjestys?")
so = sortOrder.upper()
if so == "N":
	luvut.sort()
	print(luvut)

elif so == "L": 
	luvut.sort(reverse=True)
	print(luvut)
else:
	print("Ei lajittelua. ")

# mitä tapahtuu jos käyttäjä kirjoittaa desimaalilukuja (float, esim 1.5, tai jos kirjoittaa 1,5)

