print("---------------")
print(".: Korvkollen :.")
print("----------------")
print("Hur många elever vill ha... ")

_2_korv = int(input("2 vanliga korvar      >"))
_3_korv = int(input("3 vanliga korvar      >"))
_2_vego = int(input("2 veganska korvar     >"))
_3_vego = int(input("3 veganska korvar     >"))

korv_pack = round((2 * _2_korv + 3 * _3_korv) / 8 + 0.5)
vego_pack = round((2 * _2_vego + 3 * _3_vego) / 4 + 0.5)
drick = _2_korv + _3_korv + _2_vego + _3_vego

pris = float(20.95 * porv_pack + 34.95 * vego_pack + 13.95 * drick)

print("----------------")
