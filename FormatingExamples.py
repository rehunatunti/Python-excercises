# f-formating
import math
v = math.pi
print()
print(f"Formatting Using Numeric {v = }") # Kaarisulut on f-formatingissa place holdereita

print("'<' = left-aligned.")
print("'<' = right-aligned.")
print("^ = centered.")

print(f"|{v:=25}|")
print(f"|{v:<25}|")
print(f"|{v:>25}|")
print(f"|{v:^25}|\n")

"""
v = "Python3.9"
print(f"Using string {v = }")
print(f"|{v:=25")}|")
print(f"|{v:<25")}|")
print(f"|{v:>25")}|")
print(f"|{v:^25")}|\n")

"""

print(f"Number\tSquare\tcube")
	
for x in range(1,11):
	y = x*x
	z = x*x*x
	print(f"{x:2d}\t{y:3d}\t{z:4d}")