# Ari Huttunen

"""
Ohjelma pyytää käyttäjältä yksi kokonaisluku väliltä 1 ja 10, ja laskee luvun kertoman.
Ohjelma tarkistaa, että luku on välillä 1 ja 10 ja lopettaa jos input ei ole oikea.
"""
"""Kertoma funktiolla"""

def kertoma(n):
	#print("Kertoma: ", n)
	if n==0:
		return(1)
	else: 
		return(n* kertoma(n-1))

n = int(input("Luku: "))
k = kertoma(n)
print(k)


"""Kertoma luupilla"""
"""
n = int(input("Luku: ")) 
i = 1
while i <= n:
  	f = f * i
  	i += 1
print(f)


"""