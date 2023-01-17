"""#HedelmaLista ja sen käsittely
print("Luodaan lista:")
HedelmaLista = ["omena", "banaani", "kirsikka"]
print(HedelmaLista)

#List of items indexed from the beginning
#0 refers to first item etc.
print("Tulostetaan indexin 1 hedelmä:")
print(HedelmaLista[1])

#Negative indexing means start from the end.
print("Tulostetaan viimeisestä laskien -2. hedelmä")
print(HedelmaLista[-2])

#Append
print("Lisätään appendilla \"mansikka\"")
HedelmaLista.append("mansikka")
print(HedelmaLista)

#Replace
print("korvataan indexin 1.paikan hedelmä appelsiinilla" )
(HedelmaLista[1]) = "appelsiini"
print(HedelmaLista)

#insert
HedelmaLista.insert(1, "mustikka")
print(HedelmaLista)

#Remove
HedelmaLista.remove("mansikka")
print(HedelmaLista)

#Loop in the list
for h in HedelmaLista:
	print(h)

print(len(HedelmaLista))

print("Uusi hedelmälista, newlist:")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
	if "a" in x: 
		newlist.append(x)

print(newlist)"""
	
#Dictionary, eli key-value parit

Henkilot = []
Henkilo = {
	"Enimi": "Pekka",
	"Snimi": "Puupää",
	"Svuosi": 1934,
	"SP": "M"
}

Henkilot = []
Henkilot.append(Henkilot)
Henkilo = {	
	"Enimi": "Tiina",
	"Snimi": "Tonttu",
	"Svuosi": 1936,
	"SP": "N"
}

Henkilot.append(Henkilo)
Henkilo = {
 "Enimi": "Ville",
 "Snimi": "Velho",
 "Svuosi": 1932,
 "SP": "M"
}
Henkilot.append(Henkilo)
Henkilo = {
 "Enimi": "Taru",
 "Snimi": "Olento",
 "Svuosi": 1800,
 "SP": ""
}
Henkilot.append(Henkilo)
print(Henkilot)
print("\n")

l = len(Henkilo)
i = 1
for k in Henkilo.keys():
	if i == 1: 
		print(k, end="")
	elif i == l:
		print("\t" + k)
	else:
		print("\t" + k, end="")
	i=i+1
print("-----\t-----\t-----\t-----\t")

for v in Henkilot:
	print(v["Enimi"], end="\t")
	print(v["Snimi"], end="\t")
	print(v["Svuosi"], end="\t")
	print(v["SP"])