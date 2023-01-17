# Tämä muutetaan vielä funktioilla toimivaksi

#Luvun kysyminen ja castaaminen intiksi
y = int(input("Anna luku: "))
print("Annoit luvun ", y)

#pitää olla suurempi kuin 1
if y > 1:
	#alkutekijöiden (factor) selvittäminen:
	#onko luku jaettavissa itseään pienemmillä luvuilla
	for i in range(2, y): # "range(2, y)" siis tarkoittaa, että aloittaa 2:sta ja jatkaa y:hyn asti, mutta ei sisällä y:tä
		if y % i == 0: #jakojäännös
			flag = True # siis jos jakojäännös on nolla, sijoitetaan True flag-muuttujaan

#Tarkistetaan flag-muuttujan tila
if flag == True:
	print("Luku ei ole alkuluku")
else:
	print("Luku on alkuluku")

#Tämä on tehtävissä pythonilla myös for...else lausekkeella, jolloin ei tarvita erikseen flag-muuttujaa
