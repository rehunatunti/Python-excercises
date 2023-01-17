# Kokoelma funktioita

def DisplayText(t):
	try: 
		print(t)
	except:
		print("Error")

# 2.asteen yhtälö -funktio
def q(a, b, c, d, e, f):
	import math
	d = 100
	e.append("c")
	f = "abc"
	delta = b**2 - 4*a*c # delta on tekijät neliöjuuren alla 
	print(delta)
	if delta == 0: # tällöin yhtälöllä vain yksi ratkaisu
		x = -b/2*a
		return x
	elif delta > 0: # Yhtälöllä on kaksi ratkaisua
		x1 = (-b + math.sqrt(delta))/2*a
		x2 = (-b - math.sqrt(delta))/2*a
		return x1, x2
	else:
		return ()

