class Person:
	def __init__(self, name, birthyear, sex): #initioi itsensä, funktio ottaa parametriksi kolme asiaa, self, nimi ja age
		self.name = name
		self.birthyear = birthyear
		self.sex = sex
		self.age = 30

	def __str__(self): #tämä funktio kertoo itsestään jotain, jos sitä kutsutaan
		if self.sex == 'F':
			self.age = 25
		else: 
			self.age = 2022-self.birthyear

		return f"{self.name} {self.age}"

Man = Person("John", 1960, "M")
Woman = Person("Jane", 1960, "F")

print(Man)
print(Woman)