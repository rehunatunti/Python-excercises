def q(a, b, c):
	import math
	solutions = []
	delta = b**2 - 4*a*c
	print(delta)
	if delta == 0:
		x = -b/2*a
		solutions.append(x)
		return solutions
	elif delta > 0:
		x1 = (-b + math.sqrt(delta))/2*a
		x2 = (-b - math.sqrt(delta))/2*a
		solutions.append(x1)
		solutions.append(x2)
		return solutions
	else:
		return solutions
