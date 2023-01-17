#Temperature converter

# Fahrenheit to Celsius C = F-32.00 *(5/9)
# Celsius to Fahrenheit: F = C*1.8 + 32.00

# Tee funktiot molemmille konversioille

# Kysy tuleeko Fahrenheit-Celsius vai Celsius-Fahrenheit?

print("Lämpötilan yksikkömuunnin")

#Funktiot:
def FtoC():
	try:
		f = float(input("Anna Fahrenheit-asteluku: "))
	except:
		print("Väärä syöte. Käytäthän desimaalierottimena pistettä")


	c = (5/9)*(f - 32.00)
	print(f, " Fahrenheit astetta on ", c, "Celsius-astetta.\n")
	a = input("Anna uusi luku (Y/N)?")
	if a.upper() == "Y":
		FtoC()
	else: 
		Valikko()

def CtoF():
	c = float(input("Anna Celsius-asteluku: "))
	f = c * 1.8 + 32.00
	print(c, " Celsius-astetta on ", f, " Fahrenheit-astetta.\n")
	a = input("Anna uusi luku (Y/N)?")
	if a.upper() == "Y":
		CtoF()
	else: 
		Valikko()
	
def Valikko():
	print("Valitse:")
	print("1. Fahrenheit Celsius-asteiksi")
	print("2. Celsius Fahrenheit-asteiksi")
	print("0. Lopetus\n")
	valinta = input("Valitse toiminto: ")

	if valinta == "1":
		print("Valitsit 1")
		FtoC()
	elif valinta == "2":
		print("Valitsit 2")
		CtoF()
	elif valinta == "0":
		print("Ohjelma lopetetaan.")
		exit()
	else:
		print("Väärä syöte.")
		Valikko()

#Ohjelman käynnistys:
Valikko()







