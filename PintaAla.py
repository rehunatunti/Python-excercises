import math
while True:
    choice = input("Choose a shape (t=triangle, r=rectangle, c=circle): ")
    if choice == "":
        break
    else:
        if choice.upper() == "T":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            area = (base * height) / 2
            print(f"{'The area is:':12} {area:.2f}")
        elif choice.upper() == "R":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            area = width * height
            print(f"{'The area is:':12} {area:.2f}")
        elif choice.upper() == "C":
            radius = int(input("Give radius of the circle: "))
            math.pi
            area = (radius ** 2) * math.pi
            print(f"{'The area is:':12} {area:.15f}")
        else:
            print("Unknown shape!")