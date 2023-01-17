i1 = 1
s1 = "Pekka"
l1 = ['Toytota', 'Honda']
"""i2 = 90.99
s2 = "Tiina"
l2 = ['Banana', 'Apple']"""

global i2, s2
i2 = 90.99
s2 = "Tiina"
l2 = ['Banana', 'Apple']

def ShowAndChange (i, s, l):
""" 
1. Funktion sisällä argumentit ovat paikallisia muuttujia
lukuunottamatta argumentteja, jotka on välitetty objektina
esim. lista.
2. Ainoa keino, että funktio näkee sen ulkopuolella olevat 
arvomuuttujat on määritellä ne funktion sisällä global-määreellä
globaaleiksi
"""
    print ("i1:", str(i))
    print ("s1:", s)
    print (l)
    l.append('Kia')

    #print ("i2:", str(i2))
    #print ("s2:", s2)
    print (l2)
    i2 = 100
    s2 = "Tiina"
    l2.append ("Kiwi")

ShowAndChange (i1, s1, l1)
print ("i2:", str(i2))
print ("s2:", s2)
print(l2)