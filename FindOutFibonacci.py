"""
# Ensimmäiseksi perus Fibonacci generaattori, esim ensimmäiset 5 kierrosta

print("Fibonaccin sarja, kovakoodattu")

i = 0
n = [0, 1] # Lista alustetaan kahdella luvulla, 0 ja 1.
fibo = n[-1]+n[-2] # fibo-muuttujaan sijoitetaan listan viimeisen ja toiseksi viimeisen luvun summa 

while i <= 5:
	fibo = n[-1]+n[-2]
	n.append(fibo)
	i += 1 

print("Fibonaccin 8 ensimmäistä lukua: ", n)
print("\n")
"""
"""
Tee Fibonacci-generaattori luupilla. Generaattori aloittaa tyhjästä listasta 
eli jos lista on tyhjä, if-lauseella appendataan ensimmäinen luku 0, 
ja jos ensimmäinen luku on 0, appendataan luku 1

Tee ominaisuus: ohjelma kysyy mikä on ensimmäinen luku. Toinen luku on silloin sama kuin ensimmäinen
"""
"""
"""
print("Fibonacci-generaattori\n")

i = 1
j = int(input("Montako kierrosta lasketaan? Anna luku 2-10 väliltä: "))
n = []
"""seed = input("Anna aloitusluku eli F(1)-luku 0-10 väliltä tai paina enter: ")


#if (seed == "" or int(seed) == 0):			#ei toimi oikein, jos antaa 0, menee else-haaraan
#	print(type(seed))
#	n = [0,1]
#	print("Et antanut aloituslukua, tai aloitusluku oli 0. Lukusarja alkaa näin:", n)

#else:
#	print("Aloitusluku on ", seed)
#	seed = int(seed)
#	n = [seed, seed]
#	print(type(n[1]))

	tämä ei toiminut:
	print("Aloitusluku on ", seed)
	n = [seed, seed] 		# seedin tyyppi muuttuu stringiksi
	print(type(n[1]))
	"""
	
while i <= j:
	if i == 1:
		fibo = 0
	elif i == 2:
		fibo = 1
	else: 	
		fibo = n[-1]+n[-2]
	n.append(fibo)
	i += 1

print(n)
#print("Listassa on", j+3, "lukua.")
print("Listan pituus on ", len(n))
	

""" 
Tee sama metodin avulla
"""