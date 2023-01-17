import math
a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

delta = b**2 - 4*a*c
print(delta)
if delta == 0:
	x = -b/2*a
	print(x)
elif delta > 0:
	x1 = (-b + math.sqrt(delta))/2*a
	x2 = (-b - math.sqrt(delta))/2*a
	print(x1)
	print(x2)
else:
	print("No solution")