def rodyti_skaicius(pirmas, *args):
    print(f"Pirmas: {pirmas}")
    print(f"Daugiau skaičių: {args}")

rodyti_skaicius(10, 20, 30, 40)

def gyvūnai (naminis, *zoo):
    print(f"naminis, laikomas namie: {naminis}")
    print(f"visi kiti, zoologijos sode: {zoo}")

gyvūnai("katė", "dramblys", "ožka", "tigras")

def daiktas_ir_apibudinimas (daiktas, **savybes):
    print(f"daiktas: {daiktas}")
    print(f"Spalva: {savybes}")

daiktas_ir_apibudinimas("kede", spalva1 = "raudona", spalva2 = "geltona")

