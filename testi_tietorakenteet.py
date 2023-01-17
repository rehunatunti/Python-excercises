#Dictionary
Henkilo = {
 "Enimi": "Pekka",
 "Snimi": "Puupää",
 "Svuosi": 1934,
 "SP": "M"
}
Henkilot = []
Henkilot.append(Henkilo)
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
        print(k , end="")
    elif i == l:
        print("\t" + k)
    else:
        print("\t"+ k , end="") 
    i=i+1
print("-----\t-----\t-----\t-----")

for v in Henkilot:
    print(v["Enimi"], end="\t")
    print(v["Snimi"], end="\t")
    print(v["Svuosi"], end="\t")
    print(v["SP"])
