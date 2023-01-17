#Käyttäjältä kysytään luku a ja b, kysytään a + b, a*b ja tervehdyksen tulostus
print("Tervetuloa laskuriin!")

# lukujen kysyminen
a = input("Anna luku a: ")
b = input("Anna luku b: ")
a = int(a)
b = int(b)

print("lukujen summa on", a+b)
#print(a+b)
print("Lukujen tulo on", a*b)
print("Lukujen osamäärä on",a/b)

print("\nLaskutoimitusesimerkkejä:\n")
print("1+2+3+4+5 on ", 1 + 2 + 3 + 4 + 5)
print("0.01 + 12.783 * (89 - 13) on", 0.01 + 12.783 * (89 - 13))
print("Vuodessa on:")
print(365, "päivää")
print(365 * 24, "tuntia")
print(365 * 24 * 60, "minuuttia")
print(365 * 24 * 60 * 60, "sekuntia")
print("Jos 6 lasta saavat 45 karkkia,")
print("kukin lapsi saa", 45 // 6, "karkkia")
print("ja", 45 % 6, "karkkia jää yli.")