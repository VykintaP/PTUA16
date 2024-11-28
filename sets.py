korteliu_sarasas = [432, 1, 1, 11, 123, 2, 3, 3, 124]
unikalios_korteles1 = set (korteliu_sarasas)
unikalios_korteles2 = {12, 1, 11,  213, 3, 23, 12, 12, 3121}
print ("pirma kalade:",unikalios_korteles1,
       "antra kalade:", unikalios_korteles2)

sudedu_abi_dezen = unikalios_korteles1 | unikalios_korteles2
print ("unikalios per abi kalades:",sudedu_abi_dezen)

kokios_vienodos = unikalios_korteles1 & unikalios_korteles2
print("vienodos abejose kaladese:", kokios_vienodos)

koretelei = {koretelei + 1 for koretelei in unikalios_korteles2}
print ("kortele +1 ", koretelei)

nauja_aibe = {x + 1 for x in unikalios_korteles1}
print(nauja_aibe)