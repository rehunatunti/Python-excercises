# string
print("Stringien yhdistäminen pilkulla:")
print("eka", "toka", "kolmas")

print("Stringien konkatenointi +-merkillä")
print("esi" + "merkki")
print("Konkatenoitu esi ja merkki")
print("t" + "e" + "s" + "t" + "i")
print("Konkatenoitu t + e + s + t + i")

print("Escape merkin käyttö (\\):" )
print("\"abc\" on merkkijono")
print("eka\ntoka\kolmas")
print("c:\\python\\testi.py")
print("\n")

print("nimen tulostus muuttujina (print(Etunimi, SukuNimi))")
EtuNimi = "Kalle"
SukuNimi = "Jokinen"
print(EtuNimi, SukuNimi)
print(EtuNimi + SukuNimi)
print(EtuNimi + " " + SukuNimi)

print("\n")

Title = "Built-in Data Types\n"
L1 = "Text type: \t\tstr\n"
L2 = "Numeric types: \t\tint, float, complex\n"
L3 = "Sequence types: \t\tlist, tuple, range\n"
L4 = "Mapping Types: \t\tdict\n"
L5 = "Set Types: \t\tset, frozenset\n"
Block = Title + L1 + L2 + L3 + L4 + L5
print(Block)