nimet = []
print("Anna 5 nimeä.")
for x in range(5):
	nimi = input("Nimi:")
	nimet.append(nimi)
print(nimet)

print("Tulostetaan aakkosjärjestyksessä")
for n in nimet:
	print(n)

print("Tulostetaan käänteisessä järjestyksessä (perinteisesti ohjelmoimalla)")

l = len(nimet)
x=-1
while x >-(l+1):
	print(nimet[x])
	x = x-1

# rlist-listaan ei tule jostain syystä arvoja siksi tulee 
# NoneType-object virhe 
print("Tulostettu reverse-funtion avulla")
#rlist = nimet.reverse() #Tämä ei toimi oikein
nimet.reverse()
for n in nimet:
	print(n)