# Toisen asteen yhtälö
# Importataan Funktions-tiedostosta 2.asteen yhtälöfunktio "q"
# Arvot kovakoodattuja

from Functions import q

# Tässä on varmaan testattu ylimääräisiä parametreja ja 
# kuinka ne pitää olla vastaavasti määriteltynä kysyttäväksi funktiossa

a = 1
b = -1
c = 2
d = 50
e = ["a", "b"]
f = "ab"

solutions = q(a,b,c,d,e,f)
print(d)
print(e)
print(f)
print(solutions)
l = len(solutions)

if l == 0:
	print("No solution.")
elif l == 1:
	print("x =", str(solutions[0])) 
else:
	print("x1 =", str(solutions[0]))
	print("x2 =", str(solutions[1]))  