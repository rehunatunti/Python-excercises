# Miscellaneous

#Laskurimuuttujen (i) arvon lisääminen: i += 1 (C#:ssa i ++)

import locale
locale.setlocale(locale.LC_TIME, 'fi-FI')

s = """A string
spanning over
several lines"""
s
print(s)

# python regex
# find all non alphanumeric characters: \W


#%s = jotakin str tulee tähän kohtaan, place holdereita
#% = kertoo mitkä arvot pannaan %s tilalle


print("%s concatenated with %s produces %s" % ("water", "melon", "water"+"melon"))

# toinen tapa:
w = "water"
m = "melon"
print("%s concatenated with %s produces %s" % (w, m, w+m))

# placeholderit kaarisuluissa ja järjestysnumeroilla
print("{0} concatenated with {1} produces {0}{1}".format("water", "melon"))
# toinen tapa käyttäen yllämääritettyjä muuttujia
print("{0} concatenated with {1} produces {0}{1}".format(w, m))

print(f"{'water'} concatenated with {'melon'} produces {'water' + 'melon'}")


# short hand esimerkkejä, huom. i on arvo, ei muuttuja 
i = 5
i = i+1 # tulos on 6
i += 1 # tulos on 6
i -= 1 # tulos on
i *= 10

# Potenssilaskuesimerkki
i=1
while i*i < 1000: # Ehto tarkistetaan ensin
    print("Square of", i, "is", i*i)
    i = i + 1
print("Finished printing all the squares below 1000.")

# Summataan luvut 0:sta 9:ään
s = 0

for i in [0,1,2,3,4,5,6,7,8,9]:
	s = s + i
	print("The sum is", s)


"""
1-10 kertotaulu. Koodi laskee i:n ja j:n tulon. If haara toteutuu aina vasta kun j = 10. 
Muuten mennään else-haaraan ja tulot tulostuvat samalle riville.
"""
for i in range(1,11): # i:llä on arvot 1-10
    for j in range(1,11): # j:llä on 1-10
        if j == 10:
            print (f"{i*j:4d}") # Aina kun j==10, tulee rivinvaihto
        else:
            print (f"{i*j:4d}", end="") # end="" ansiosta ei tule rivinvaihtoa


# for-looppi ja break
# kokeile vaihtaa negatiiviset pois
#l = [1,3,65,3,-1,56,-10]

l=[1,3,65,3,1,56,10]
print(l)
for x in l:
    if x < 0:
        break
if x < 0:
	print("The first negative list element was", x)
else: 
	print("No negative value")

# Sama lista lukuja, mutta kysytään logaritmi ja neliöjuuri
from math import sqrt, log
l=[1,0,3,65,3,-1,56,-10]
print()
print(l)
for x in l:
	if x < 0:
		continue # eli hypätään negatiivisten yli tässä tapauksessa
	elif x == 0: # saadaan neliöjuuri, mutta ei logaritmia.
		print(f"Square root of {x} is {sqrt(x):.3f}")
		print(f"Natural logarithm of {x} is not defined.")
	else: 
		print(f"Square root of {x} is {sqrt(x):.3f}")
		print(f"Natural logarithm of {x} is {log(x):.4f}")

# Funktio, joka kertoo argumenttinsa kahdella. docstring funktion dokumentaatioesimerkkinä.
# doctstring tulostetaan .__doc__ avulla. Myös help(funktionnimi) toimii.
def double(x):
	"This function multiplies its argument by two." # Tämä on docstring, funktion dokumentaatiota
	return x*2 

print(double(4), double(1.2), double("abc")) # It even happens to work for strings!
print("The docstring is:", double.__doc__) 
help(double)   # Another way to access the docstring


#Using tuples and arguments packing
def sum_of_squares(*t):
    "Computes the sum of squares of arbitrary number of arguments"
    s=0
    for x in t:
        s += x**2
    return s
print(sum_of_squares(-2))
print(sum_of_squares(-2,4,5))

# funktiolle argumentit välitetään tuplena, määrä voi olla vaihteleva, arvot erotetaan pilkulla.